"""ETL Assets for Dagster pipeline."""

import base64
import datetime
import json
import os
import zoneinfo

# TODO: skdとしてインポートする
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from urllib.parse import urlparse
from uuid import UUID

import boto3  # type: ignore
import uuid6
from dagster import (
    AssetExecutionContext,
    AssetSpec,
    Config,
    DynamicPartitionsDefinition,
    Output,
    asset,
    multi_asset,
)
from dagster_aws.pipes import PipesECSClient, PipesGlueClient, PipesLambdaClient


class QDevClient(ABC):
    """
    Base class for QDev client operations.
    This class defines the interface for extracting, transforming, and indexing data.
    Subclasses should implement the `transform` and `index` methods.
    """
    @abstractmethod
    def extract(self, type: str) -> Output:
        pass
    
    @abstractmethod
    def transform(self) -> Output:
        pass
    
    @abstractmethod
    def index(self) -> Output:
        pass


@asset(
    deps=["crawled_files"],
    kinds={"s3", "bronze", "python"},
)
def example_s3_bronze_asset() -> Output:
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return Output(
        value={"hoge": "fuga"},
        tags={"start_url_hostname": "example.com"},
    )

class ExampleS3SilverConfig(Config):
    user_id: str

@asset(
    deps=[example_s3_bronze_asset],
    kinds={"s3", "silver", "python"},
)
def example_s3_silver_asset(
    context: AssetExecutionContext,
    example_s3_bronze_asset: Dict[str, Any],
    qdev_client: QDevClient,
) -> Output:
    """Example asset that transforms the bronze asset into a silver asset."""

    # Example transformation logic
    transformed_data = {
        "piyo": example_s3_bronze_asset["hoge"],
        "timestamp": datetime.datetime.now(tz=zoneinfo.ZoneInfo("Asia/Tokyo")).isoformat(),
    }

    return Output(
        value=transformed_data,
    )

@asset(
    deps=["example_s3_silver_asset"],
    kinds={"s3", "gold", "python"},
)
def example_s3_glod_asset() -> Output:
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return Output(
        value={"hoge": "fuga"},
        tags={"start_url_hostname": "example.com"},
    )

