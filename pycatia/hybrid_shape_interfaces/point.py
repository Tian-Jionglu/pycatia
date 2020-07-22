#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape
from pycatia.system_interfaces.system_service import SystemService


class Point(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         Point
                | 
                | Represents the hybrid shape Point feature object.
                | Role: Declare hybrid shape Point root feature object. All interfaces for
                | different type of Point derives HybridShapePoint.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePoint
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.point_ = com_object

    def get_coordinates(self) -> tuple:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCoordinates(CATSafeArrayVariant oCoordinates)
                | 
                |     Gets cartesian coordinates of the Point.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             coordinates of the Point.
                | 
                |     See also:
                |         HybridShapeFactory

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = 'get_coordinates'
        vba_code = """
        Public Function get_coordinates(point)
            Dim oCoordinates (2)
            point.GetCoordinates oCoordinates
            get_coordinates = oCoordinates
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_coordinates(self, o_coordinates: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetCoordinates(CATSafeArrayVariant oCoordinates)
                | 
                |     Sets cartesian coordinates of the point.
                |     Note: SetCoordinates can only be used on CATIAHybridShapePointCoord
                |     feature
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             coordinates of the point.
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_coordinates:
        :return: None
        :rtype: None
        """
        return self.point_.SetCoordinates(o_coordinates)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_coordinates'
        # # vba_code = """
        # # Public Function set_coordinates(point)
        # #     Dim oCoordinates (2)
        # #     point.SetCoordinates oCoordinates
        # #     set_coordinates = oCoordinates
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Point(name="{self.name}")'
