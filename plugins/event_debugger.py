import logging

logger = logging.getLogger(__name__)


class Plugin:
    def __init__(self, bus):
        bus.subscribe(self.process_event, thread=True)

    def process_event(self, ev):
        logger.debug("%s: %s", ev.name, str(ev.data))
