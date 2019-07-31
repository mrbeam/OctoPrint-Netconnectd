
class Analytics:
    ANALYTICS_DATA = 'MrbAnalyticsData'
    EVENT_WIFI_CONFIG = 'wifi_config'
    EVENT_WIFI_REFRESH = 'wifi_refresh'

    def __init__(self, plugin):
        self._plugin = plugin
        self._logger = self._plugin._logger

    def write_wifi_config_command(self, command, success, err=None):
        try:
            data = dict(
                command=command,
                success=success,
                err=err,
            )
            self._send_op_event(eventname=self.EVENT_WIFI_CONFIG, data=data)
        except:
            self._logger.exception("Exception while writing wifi config command to analytics.")

    def _send_op_event(self, eventname, data):
        payload = dict(
            plugin='netconnectd',
            eventname=eventname,
            data=data
        )
        self._plugin._event_bus.fire(self.ANALYTICS_DATA, payload)
