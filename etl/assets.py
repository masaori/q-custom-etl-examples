"""ETL Assets for Dagster pipeline."""

import base64
import datetime
import json
import os
import zoneinfo
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


@asset(
    kinds={"s3", "bronze", "python"},
)
def example_s3_bronze_asset() -> Output:
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return Output(
        value={"hoge": "fuga"},
        tags={"start_url_hostname": "example.com"},
    )