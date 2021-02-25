from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument

# document_type is used to mapping document's name to type
document_type = {
    'CATPart': PartDocument,
    'CATProduct': ProductDocument,
    'CATSystem': FunctionalDocument
}