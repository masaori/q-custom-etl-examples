"""ETL Assets for Dagster pipeline."""

from dagster import asset, AssetExecutionContext # type: ignore
from dagster_qint import QintClient, UrlListConfig

@asset(
    deps=[],
    kinds={"s3", "bronze", "python"},
)
def example_s3_bronze_asset(
    context: AssetExecutionContext,
    qint_client: QintClient,
):
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return qint_client.extract(
        context=context,
        source_type="url_list",
        config=UrlListConfig(
            url_list_id="example_s3_bronze_asset",
            user_id="aaa",
            urls=["https://example.com/data1.json", "https://example.com/data2.json"],
        ),
    )
