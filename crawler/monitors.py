from spidermon import Monitor, MonitorSuite, monitors


@monitors.name("Item Count")
class ItemCountMonitor(Monitor):
    def test_item_count(self):
        count = self.data.stats.get("item_scraped_count", 0)
        assert count >= 10, f"Expected at least 10 items, got {count}"


class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [ItemCountMonitor]
