
from prometheus_client import CollectorRegistry, Counter, Histogram, push_to_gateway
from prometheus_client.core import CounterMetricFamily

DEST = "localhost:9091"
registry = CollectorRegistry()

# nginx_ingress_controller_response_duration_seconds_bucket

class CustomCollector(object):
    def collect(self):
        counter_metric = CounterMetricFamily(
            name="http_response_duration_seconds_test_bucket", documentation="None", labels=["label1", "label2"])
        counter_metric.add_metric(labels=["label11", "label22"], value=1.0)
        yield counter_metric



def main():
    job_name = "research_histogram_percentile"
    registry.register(CustomCollector()) # type: ignore
    push_to_gateway(DEST, job=job_name, registry=registry)


if __name__ == '__main__':
    main()
