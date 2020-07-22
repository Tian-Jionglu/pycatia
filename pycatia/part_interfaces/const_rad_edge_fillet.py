#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.edge_fillet import EdgeFillet


class ConstRadEdgeFillet(EdgeFillet):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 PartInterfaces.EdgeFillet
                |                                     ConstRadEdgeFillet
                | 
                | Represents the edge fillet shape with a constant radius.
                | The resulting shape is made up of edge fillets built with a constant
                | radius.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.const_rad_edge_fillet = com_object

    @property
    def objects_to_fillet(self) -> References:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ObjectsToFillet() As References (Read Only)
                | 
                |     Returns the collection of reference elements to be
                |     filleted.
                | 
                |     Example:
                |         The following example returns in elements the reference elements to be
                |         filleted of the constant radius edge fillet
                |         firstCstEdgeFillet:
                | 
                |          Set elements = firstCstEdgeFillet.ObjectsToFillet

        :return: References
        :rtype: References
        """

        return References(self.const_rad_edge_fillet.ObjectsToFillet)

    @property
    def radius(self) -> Length:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the edge fillet constant radius.
                | 
                |     Example:
                |         The following example returns in radius the radius of the constant
                |         radius edge fillet firstCstEdgeFillet:
                | 
                |          Set radius = firstCstEdgeFillet.Radius

        :return: Length
        :rtype: Length
        """

        return Length(self.const_rad_edge_fillet.Radius)

    def add_object_to_fillet(self, i_object_to_fillet: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddObjectToFillet(Reference iObjectToFillet)
                | 
                |     Adds a new sub-element to be filleted. This sub-element is usually an
                |     edge.
                | 
                |     Parameters:
                | 
                |         iObjectToFillet
                |             The sub-element to be filleted
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example adds a new geometrical element element to be filleted
                |     by the constant radius edge fillet firstCstEdgeFillet:
                | 
                |      firstCstEdgeFillet.AddObjectToFillet(element)

        :param Reference i_object_to_fillet:
        :return: None
        :rtype: None
        """
        return self.const_rad_edge_fillet.AddObjectToFillet(i_object_to_fillet.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_object_to_fillet'
        # # vba_code = """
        # # Public Function add_object_to_fillet(const_rad_edge_fillet)
        # #     Dim iObjectToFillet (2)
        # #     const_rad_edge_fillet.AddObjectToFillet iObjectToFillet
        # #     add_object_to_fillet = iObjectToFillet
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_object_to_fillet(self, i_object_to_withdraw: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawObjectToFillet(Reference iObjectToWithdraw)
                | 
                |     Withdraws a sub-element from those to be filleted. This sub-element is
                |     usually an edge.
                | 
                |     Parameters:
                | 
                |         iObjectToWithdraw
                |             The sub-element to withdraw
                |             The following 
                | 
                |         Boundary object is supported: TriDimFeatEdge. 
                | 
                | Example:
                |     The following example withdraws the geometrical element element from those
                |     to be filleted by the constant radius edge fillet
                |     firstCstEdgeFillet:
                | 
                |      firstCstEdgeFillet.WithdrawObjectToFillet(element)

        :param Reference i_object_to_withdraw:
        :return: None
        :rtype: None
        """
        return self.const_rad_edge_fillet.WithdrawObjectToFillet(i_object_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_object_to_fillet'
        # # vba_code = """
        # # Public Function withdraw_object_to_fillet(const_rad_edge_fillet)
        # #     Dim iObjectToWithdraw (2)
        # #     const_rad_edge_fillet.WithdrawObjectToFillet iObjectToWithdraw
        # #     withdraw_object_to_fillet = iObjectToWithdraw
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ConstRadEdgeFillet(name="{self.name}")'
