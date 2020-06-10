#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle


class HybridShapePlaneAngle(Plane):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneAngle
                | 
                | Represents the hybrid shape plane angle feature object.
                | Role: To access the data of the hybrid shape plane angle feature object,
                | created with an angle to another plane. This data includes:
                | 
                |     The rotation axis
                |     The rotation angle
                |     The reference plane
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlaneAngle
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_angle = com_object

    @property
    def angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Angle() As Angle (Read Only)
                | 
                |     Returns the rotation angle.

        :return: Angle
        """

        return Angle(self.hybrid_shape_plane_angle.Angle)

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Orientation() As long
                | 
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

        :return: int
        """

        return self.hybrid_shape_plane_angle.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_plane_angle.Orientation = value

    @property
    def plane(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_angle.Plane)

    @plane.setter
    def plane(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_angle.Plane = value

    @property
    def projection_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ProjectionMode() As boolean
                | 
                |     Gets or sets the projection mode status. ProjectionMode = TRUE : Rotation axis will be projected on to reference plane. = FALSE(default) : Rotation axis will be as it is. This example retrieves in ProjMode the projection mode status for the PlaneAngle hybrid shape feature.
                | 
                |      Dim ProjMode As boolean
                |      ProjMode = PlaneAngle.ProjectionMode

        :return: bool
        """

        return self.hybrid_shape_plane_angle.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_plane_angle.ProjectionMode = value

    @property
    def revol_axis(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RevolAxis() As Reference
                | 
                |     Returns or sets the rotation axis.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     RectilinearBiDimFeatEdge or RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_angle.RevolAxis)

    @revol_axis.setter
    def revol_axis(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_angle.RevolAxis = value

    def __repr__(self):
        return f'HybridShapePlaneAngle(name="{ self.name }")'