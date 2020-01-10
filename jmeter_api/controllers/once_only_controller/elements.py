from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str
from xml.etree.ElementTree import Element, ElementTree, tostring
from xml.sax.saxutils import unescape
from typing import List, Optional
from xml.sax.saxutils import unescape
from settings import logging
import os


class OnceOnlyController(BasicController, Renderable):

    root_element_name = 'OnceOnlyController'
    TEMPLATE = 'once_only_controller_template.xml'

    def __init__(self, *,
                 name: str = 'Once Only Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         


    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
