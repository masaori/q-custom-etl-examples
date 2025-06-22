"""ETL Assets for Dagster pipeline."""

from dagster import asset, AssetExecutionContext # type: ignore
from dagster_qbiz import QbizClient, UrlListConfig

@asset(
    kinds={"s3", "bronze", "python"},
)
def ir_document_url_list(
    context: AssetExecutionContext,
    qbiz_client: QbizClient,
    config: UrlListConfig,
):
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return qbiz_client.extract(
        context=context,
        source_type="url_list",
        config=config,
    )

@asset(
    deps=["ir_document_url_list"],
    kinds={"s3", "bronze", "python"},
)
def test_transform(
    context: AssetExecutionContext,
    qbiz_client: QbizClient,
    config: UrlListConfig,
):
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return qbiz_client.transform(
        context=context,
        script_path="custom_transform.py",
    )

