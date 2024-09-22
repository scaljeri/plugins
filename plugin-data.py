from hansken_extraction_plugin.api.extraction_plugin import ExtractionPlugin, MetaExtractionPlugin, DeferredExtractionPlugin
from hansken_extraction_plugin.api.plugin_info import Author, MaturityLevel, PluginId, PluginInfo
from hansken_extraction_plugin.runtime.extraction_plugin_runner import run_with_hanskenpy
from logbook import Logger

log = Logger(__name__)


class Plugin(ExtractionPlugin):

    def plugin_info(self):
        plugin_info = PluginInfo(
            id=PluginId(domain='my-domain', category='yolo', name='Count_ab'),
            version='0.0.1',
            description='Count the numner of a\'s en meer',
            author=Author('Me', 'foo@bar', 'Work'),
            maturity=MaturityLevel.PROOF_OF_CONCEPT,
            webpage_url='',  # e.g. url to the code repository of your plugin
            matcher='file.extension=txt AND $data.type=raw',  # add the query for the types of traces your plugin should match
            # matcher='toolrun.tool=ocr,file.extension=txt',  # add the query for the types of traces your 
            # matcher='file.extension=txt',  # add the query for the types of traces your 
            license='Apache License 2.0'
        )
        return plugin_info

    def process(self, trace, data_context):
        log.info(f"processing trace {trace.get('name')} {data_context.data_type}")
        # Add your plugin implementation here
        count = 0

        data = trace.open().read(data_context.data_size).decode('utf-8')

        for line in data:
            line = line.lower()
            count += line.count('a')

        trace.update({'file.misc.count3x': str(count)})

if __name__ == '__main__':
    # optional main method to run your plugin with Hansken.py
    # see detail at:
    #  https://netherlandsforensicinstitute.github.io/hansken-extraction-plugin-sdk-documentation/latest/dev/python/hanskenpy.html
    run_with_hanskenpy(Plugin)
