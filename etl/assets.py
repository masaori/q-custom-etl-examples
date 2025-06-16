"""ETL Assets for Dagster pipeline."""

from dagster import asset, AssetExecutionContext # type: ignore
from dagster_qint import QintClient, UrlListConfig

@asset(
    kinds={"s3", "bronze", "python"},
)
def ir_document_url_list(
    context: AssetExecutionContext,
    qint_client: QintClient,
    config: UrlListConfig,
):
    """Example asset that reads from S3 and returns a list of dictionaries."""

    return qint_client.extract(
        context=context,
        source_type="url_list",
        config=config,
    )
