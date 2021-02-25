#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.collection import Collection
from pycatia.funct_system_interfaces.functional_variant import FunctionalVariant
from pycatia.types import cat_variant

class FunctionalVariants(Collection):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FunctionalVariants
                | 
                | The interface to access a collection of FunctionalVariants.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_variants = com_object

    def create(self, i_name: str) -> FunctionalVariant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create(CATBSTR iName) As FunctionalVariant
                | 
                |     Create a FunctionalVariant.

        :param str i_name:
        :return: FunctionalVariant
        :rtype: FunctionalVariant
        """
        return FunctionalVariant(self.functional_variants.Create(i_name))

    def delete(self, i_variant: FunctionalVariant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Delete(FunctionalVariant iVariant)
                | 
                |     Delete a FunctionalVariant.

        :param FunctionalVariant i_variant:
        :return: None
        :rtype: None
        """
        return self.functional_variants.Delete(i_variant.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete'
        # # vba_code = """
        # # Public Function delete(functional_variants)
        # #     Dim iVariant (2)
        # #     functional_variants.Delete iVariant
        # #     delete = iVariant
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def elem(self, i_index: cat_variant) -> FunctionalVariant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Elem(CATVariant iIndex) As FunctionalVariant
                | 
                |     Returns a Variant using its index or its name from the Variants
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Variant to retrieve from the
                |             collection of Variants. As a numerics, this index is the rank of the Variant in
                |             the collection. The index of the first Variant in the collection is 1, and the
                |             index of the last Variant is Count. As a string, it is the name you assigned to
                |             the Variant using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Variant 
                |     Example:
                |         This example retrieves in Act1 the fifth Variant in the collection and
                |         in Act2 the Variant named Moves.
                | 
                |          Dim Act1 As FunctionalVariant
                |          Set Act1 = Desc.Variant(5)
                |          Dim Act2 As FunctionalVariant
                |          Set Act2 = Desc.Variant("Adding new substance")

        :param CATVariant i_index:
        :return: FunctionalVariant
        :rtype: FunctionalVariant
        """
        return FunctionalVariant(self.functional_variants.Elem(i_index.com_object))

    def __iter__(self):
        for i in range(self.count):
            yield FunctionalVariant(self.com_object.Elem(i + 1))

    def __repr__(self):
        return f'FunctionalVariants(name="{ self.name }")'