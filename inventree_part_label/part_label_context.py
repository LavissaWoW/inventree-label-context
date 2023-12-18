"""Plugin to get all default parts for a given stock location"""
from plugin import InvenTreePlugin
from plugin.mixins import ReportMixin
from label.models import StockLocationLabel
from part.models import Part
from part.serializers import PartBriefSerializer
 
class DefaultLocationContext(ReportMixin, InvenTreePlugin):
    """Plugin to get Default Parts added to label context"""
    
    AUTHOR = "Lavissa"
    NAME = "Default Location context"
    SLUG = "defaultlocationcontext"
    TITLE = "Default Location context"
    DESCRIPTION = "Plugin to get Default Parts added to label context"
    VERSION = "0.1"
    MIN_VERSION = "0.13.0"
#    MAX_VERSION = "0.13.0" #This plugin will be phased out when this is added to InvenTree Core
    
    def get_default_parts(self, pk):
        parts = Part.objects.all().filter(default_location=pk)
        
        serializer = PartBriefSerializer(parts, many=True)
                    
        return serializer.data
    
    def add_label_context(self, label_instance, instance, request, context):
        if isinstance(label_instance, StockLocationLabel):
            context['default_parts'] = self.get_default_parts(instance.pk)