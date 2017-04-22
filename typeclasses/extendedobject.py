""" An Extended object to include sensory components"""
from objects import Object

class ExtendedObject(Object):
    """
    This simple object defines some attributes and
    """
    def at_object_creation(self):
        """
        Called when object is created. We make sure to set the needed
        Attributes.
        """
        super(ExtendedObject, self).at_object_creation()
        self.db.readable_text = "There is no text written on %s." % self.key
        self.db.feelable_text = "You do not feel anything special about %s." % self.key
        self.db.tasteable_text = "%s doesn't taste like anything." % self.key
        self.db.smellable_text = "%s doesn't smell like anything." % self.key
        
        