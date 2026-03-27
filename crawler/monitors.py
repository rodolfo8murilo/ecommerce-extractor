from spidermon import Monitor, MonitorSuite, monitors


@monitors.name("Item Count")
class ItemCountMonitor(Monitor):
    def test_item_count(self):
        count = self.data.stats.get("item_scraped_count", 0)
        assert count >= 1, f"Expected at least 1 items, got {count}"


class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [ItemCountMonitor]
