from hansken_extraction_plugin.api.extraction_plugin import ExtractionPlugin, MetaExtractionPlugin, DeferredExtractionPlugin, MetaExtractionTrace
from hansken_extraction_plugin.api.plugin_info import Author, MaturityLevel, PluginId, PluginInfo
from hansken_extraction_plugin.runtime.extraction_plugin_runner import run_with_hanskenpy
from logbook import Logger

log = Logger(__name__)

handler = logging.StreamHandler()
# logbook.StreamHandler(level=logbook.INFO).push_application()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set the logging level
# logbook.CRITICAL
# logbook.ERROR
# logbook.WARNING
# logbook.NOTICE
# logbook.INFO
# logbook.DEBUG
# logbook.TRACE
logger.setLevel(logging.INFO)

# Log some messages
logger.info('This is an info message')
logger.error('This is an error message')


class Plugin(MetaExtractionPlugin):

    def plugin_info(self):
        plugin_info = PluginInfo(
            id=PluginId(domain='my-domain', category='yolo', name='Count_ab'),
            version='0.0.1',
            description='Count the numner of a\'s en meer',
            author=Author('Me', 'me@me', 'Yolo'),
            maturity=MaturityLevel.PROOF_OF_CONCEPT,
            webpage_url='',  # e.g. url to the code repository of your plugin
            matcher='file.extension=txt',  # add the query for the types of traces your plugin should match
            # matcher='toolrun.tool=ocr,file.extension=txt',  # add the query for the types of traces your 
            # matcher='file.extension=txt',  # add the query for the types of traces your 
            license='Apache License 2.0'
        )
        return plugin_info

    def process(self, trace: MetaExtractionTrace):
        log.info(f"processing trace {trace.get('name')}")
        print(f"{type(trace)}\n{trace.__dict__}\n{dir(trace)}")
        # Add your plugin implementation here
        count = 0
        # output = dict(trace.get('user.extracted.file'))
        # print(f"YOLO={output['misc']}\n")
        output = trace.get('classification')
        print(f"YOLO={output}\n")
        # output['misc']['count'] = 99
        # print(f"OUTPUT {output['misc']['count']}")
        # trace.update({ 'file.misc.count2':'991'})
        # trace.update({ 'user.processed.file.misc.count2':'9911'})
        # trace.update('classification', {'modelName': 'auto'})
        # trace.update('classification')
        trace.add_tracelet('classification', {'modelName': 'auto'})

        # trace.update({'file.misc.count3x': str(count)})

if __name__ == '__main__':
    # optional main method to run your plugin with Hansken.py
    # see detail at:
    #  https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/hanskenpy.html
    run_with_hanskenpy(Plugin)
