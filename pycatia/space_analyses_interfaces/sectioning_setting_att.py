#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SectioningSettingAtt(SettingController):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         SectioningSettingAtt
                | 
                | The interface to access a CATIASectioningSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sectioning_setting_att = com_object

    @property
    def clipping_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ClippingMode() As CatSectionClippingMode
                | 
                |     Returns or sets the ClippingMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: enum cat_section_clipping_mode
        """

        return self.sectioning_setting_att.ClippingMode

    @clipping_mode.setter
    def clipping_mode(self, value):
        """
        :param enum cat_section_clipping_mode value:
        """

        self.sectioning_setting_att.ClippingMode = value

    @property
    def display_cut_in_wireframe(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DisplayCutInWireframe() As boolean
                | 
                |     Returns or sets the DisplayCutInWireframe parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.DisplayCutInWireframe

    @display_cut_in_wireframe.setter
    def display_cut_in_wireframe(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.DisplayCutInWireframe = value

    @property
    def grid_auto_filtering(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridAutoFiltering() As boolean
                | 
                |     Returns or sets the GridAutoFiltering parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.GridAutoFiltering

    @grid_auto_filtering.setter
    def grid_auto_filtering(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.GridAutoFiltering = value

    @property
    def grid_auto_resize(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridAutoResize() As boolean
                | 
                |     Returns or sets the GridAutoResize parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.GridAutoResize

    @grid_auto_resize.setter
    def grid_auto_resize(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.GridAutoResize = value

    @property
    def grid_height_step(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridHeightStep() As float
                | 
                |     Returns or sets the GridHeightStep parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: float
        """

        return self.sectioning_setting_att.GridHeightStep

    @grid_height_step.setter
    def grid_height_step(self, value):
        """
        :param float value:
        """

        self.sectioning_setting_att.GridHeightStep = value

    @property
    def grid_position_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridPositionMode() As CatGridPositionMode
                | 
                |     Returns or sets the GridPositionMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: enum cat_grid_position_mode
        """

        return self.sectioning_setting_att.GridPositionMode

    @grid_position_mode.setter
    def grid_position_mode(self, value):
        """
        :param enum cat_grid_position_mode value:
        """

        self.sectioning_setting_att.GridPositionMode = value

    @property
    def grid_style(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridStyle() As CatSectionGridStyle
                | 
                |     Returns or sets the GridStyle parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: enum cat_section_grid_style
        """

        return self.sectioning_setting_att.GridStyle

    @grid_style.setter
    def grid_style(self, value):
        """
        :param enum cat_section_grid_style value:
        """

        self.sectioning_setting_att.GridStyle = value

    @property
    def grid_width_step(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GridWidthStep() As float
                | 
                |     Returns or sets the GridWidthStep parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: float
        """

        return self.sectioning_setting_att.GridWidthStep

    @grid_width_step.setter
    def grid_width_step(self, value):
        """
        :param float value:
        """

        self.sectioning_setting_att.GridWidthStep = value

    @property
    def hide_plane(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HidePlane() As boolean
                | 
                |     Returns or sets the HidePlane parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.HidePlane

    @hide_plane.setter
    def hide_plane(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.HidePlane = value

    @property
    def hide_result(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property HideResult() As boolean
                | 
                |     Returns or sets the HideResult parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.HideResult

    @hide_result.setter
    def hide_result(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.HideResult = value

    @property
    def plane_normal(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PlaneNormal() As CatSectionPlaneNormal
                | 
                |     Returns or sets the PlaneNormal parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: enum cat_section_plane_normal
        """

        return self.sectioning_setting_att.PlaneNormal

    @plane_normal.setter
    def plane_normal(self, value):
        """
        :param enum cat_section_plane_normal value:
        """

        self.sectioning_setting_att.PlaneNormal = value

    @property
    def plane_origin(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PlaneOrigin() As CatSectionPlaneOrigin
                | 
                |     Returns or sets the PlaneOrigin parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: enum cat_section_plane_origin
        """

        return self.sectioning_setting_att.PlaneOrigin

    @plane_origin.setter
    def plane_origin(self, value):
        """
        :param enum cat_section_plane_origin value:
        """

        self.sectioning_setting_att.PlaneOrigin = value

    @property
    def section_export_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SectionExportType() As boolean
                | 
                |     Returns or sets the SectionExportType parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.SectionExportType

    @section_export_type.setter
    def section_export_type(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.SectionExportType = value

    @property
    def section_fill(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SectionFill() As boolean
                | 
                |     Returns or sets the SectionFill parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.SectionFill

    @section_fill.setter
    def section_fill(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.SectionFill = value

    @property
    def update_result(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UpdateResult() As boolean
                | 
                |     Returns or sets the UpdateResult parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.UpdateResult

    @update_result.setter
    def update_result(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.UpdateResult = value

    @property
    def viewer_auto_open(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ViewerAutoOpen() As boolean
                | 
                |     Returns or sets the ViewerAutoOpen parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.ViewerAutoOpen

    @viewer_auto_open.setter
    def viewer_auto_open(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.ViewerAutoOpen = value

    @property
    def viewer_auto_reframe(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ViewerAutoReframe() As boolean
                | 
                |     Returns or sets the ViewerAutoReframe parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.ViewerAutoReframe

    @viewer_auto_reframe.setter
    def viewer_auto_reframe(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.ViewerAutoReframe = value

    @property
    def viewer_lock2_d(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ViewerLock2D() As boolean
                | 
                |     Returns or sets the ViewerLock2D parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :return: bool
        """

        return self.sectioning_setting_att.ViewerLock2D

    @viewer_lock2_d.setter
    def viewer_lock2_d(self, value):
        """
        :param bool value:
        """

        self.sectioning_setting_att.ViewerLock2D = value

    @property
    def window_default_height(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WindowDefaultHeight() As long
                | 
                | 
                |     Role:Retrieve section window default height if the window open mode is
                |     catSecWindow_DefaultSize
                | 
                |     Parameters:
                | 
                |         oWindowDefaultHeight
                | 
                |     Returns:
                |         S_OK Successfully retieved the window open mode E_FAIL Failed to
                |         retrieved the window open mode

        :return: int
        """

        return self.sectioning_setting_att.WindowDefaultHeight

    @window_default_height.setter
    def window_default_height(self, value):
        """
        :param int value:
        """

        self.sectioning_setting_att.WindowDefaultHeight = value

    @property
    def window_default_width(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WindowDefaultWidth() As long
                | 
                | 
                |     Role:Retrieve section window default width if the window open mode is
                |     catSecWindow_DefaultSize
                | 
                |     Parameters:
                | 
                |         oWindowDefaultWidth
                | 
                |     Returns:
                |         S_OK Successfully retieved the window open mode E_FAIL Failed to
                |         retrieved the window open mode

        :return: int
        """

        return self.sectioning_setting_att.WindowDefaultWidth

    @window_default_width.setter
    def window_default_width(self, value):
        """
        :param int value:
        """

        self.sectioning_setting_att.WindowDefaultWidth = value

    @property
    def window_open_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property WindowOpenMode() As CatSecWindowOpenMode
                | 
                | 
                |     Role:Retrieve section window open mode
                | 
                |     Parameters:
                | 
                |         oWindowOpenMode
                |             Legal values:
                |             catSecWindow_DefaultSize :Opens the sectioning window(s) with the
                |             default size specified in the Tools->Options.
                |             catSecWindow_TileVertically :Tiles the sectioning window(s)
                |             vertically in the viewer 
                | 
                |     Returns:
                |         S_OK Successfully retieved the window open mode E_FAIL Failed to
                |         retrieved the window open mode

        :return: enum cat_sec_window_open_mode
        """

        return self.sectioning_setting_att.WindowOpenMode

    @window_open_mode.setter
    def window_open_mode(self, value):
        """
        :param enum cat_sec_window_open_mode value:
        """

        self.sectioning_setting_att.WindowOpenMode = value

    def get_clipping_mode_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetClippingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ClippingMode
                |     parameter.
                |     Role:Retrieves the state of the ClippingMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetClippingModeInfo(io_admin_level, io_locked)

    def get_display_cut_in_wireframe_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDisplayCutInWireframeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DisplayCutInWireframe
                |     parameter.
                |     Role:Retrieves the state of the DisplayCutInWireframe parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetDisplayCutInWireframeInfo(io_admin_level, io_locked)

    def get_grid_auto_filtering_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridAutoFilteringInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridAutoFiltering
                |     parameter.
                |     Role:Retrieves the state of the GridAutoFiltering parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridAutoFilteringInfo(io_admin_level, io_locked)

    def get_grid_auto_resize_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridAutoResizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridAutoResize
                |     parameter.
                |     Role:Retrieves the state of the GridAutoResize parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridAutoResizeInfo(io_admin_level, io_locked)

    def get_grid_height_step_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridHeightStepInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridHeightStep
                |     parameter.
                |     Role:Retrieves the state of the GridHeightStep parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridHeightStepInfo(io_admin_level, io_locked)

    def get_grid_position_mode_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridPositionModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridPositionMode
                |     parameter.
                |     Role:Retrieves the state of the GridPositionMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridPositionModeInfo(io_admin_level, io_locked)

    def get_grid_style_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridStyleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridStyle
                |     parameter.
                |     Role:Retrieves the state of the GridStyle parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridStyleInfo(io_admin_level, io_locked)

    def get_grid_width_step_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetGridWidthStepInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the GridWidthStep
                |     parameter.
                |     Role:Retrieves the state of the GridWidthStep parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetGridWidthStepInfo(io_admin_level, io_locked)

    def get_hide_plane_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetHidePlaneInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the HidePlane
                |     parameter.
                |     Role:Retrieves the state of the HidePlane parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetHidePlaneInfo(io_admin_level, io_locked)

    def get_hide_result_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetHideResultInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the HideResult
                |     parameter.
                |     Role:Retrieves the state of the HideResult parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetHideResultInfo(io_admin_level, io_locked)

    def get_plane_color(self, o_r=None, o_g=None, o_b=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPlaneColor(long oR,
                | long oG,
                | long oB)
                | 
                |     Returns the PlaneColor parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :return: None
        """
        return self.sectioning_setting_att.GetPlaneColor(o_r, o_g, o_b)

    def get_plane_color_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PlaneColor
                |     parameter.
                |     Role:Retrieves the state of the PlaneColor parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetPlaneColorInfo(io_admin_level, io_locked)

    def get_plane_normal_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneNormalInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PlaneNormal
                |     parameter.
                |     Role:Retrieves the state of the PlaneNormal parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetPlaneNormalInfo(io_admin_level, io_locked)

    def get_plane_origin_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPlaneOriginInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PlaneOrigin
                |     parameter.
                |     Role:Retrieves the state of the PlaneOrigin parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetPlaneOriginInfo(io_admin_level, io_locked)

    def get_section_export_type_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSectionExportTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SectionExportType
                |     parameter.
                |     Role:Retrieves the state of the SectionExportType parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetSectionExportTypeInfo(io_admin_level, io_locked)

    def get_section_fill_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSectionFillInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SectionFill
                |     parameter.
                |     Role:Retrieves the state of the SectionFill parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetSectionFillInfo(io_admin_level, io_locked)

    def get_update_result_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetUpdateResultInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UpdateResult
                |     parameter.
                |     Role:Retrieves the state of the UpdateResult parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetUpdateResultInfo(io_admin_level, io_locked)

    def get_viewer_auto_open_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetViewerAutoOpenInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewerAutoOpen
                |     parameter.
                |     Role:Retrieves the state of the ViewerAutoOpen parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetViewerAutoOpenInfo(io_admin_level, io_locked)

    def get_viewer_auto_reframe_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetViewerAutoReframeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewerAutoReframe
                |     parameter.
                |     Role:Retrieves the state of the ViewerAutoReframe parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetViewerAutoReframeInfo(io_admin_level, io_locked)

    def get_viewer_lock2_d_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetViewerLock2DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewerLock2D
                |     parameter.
                |     Role:Retrieves the state of the ViewerLock2D parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetViewerLock2DInfo(io_admin_level, io_locked)

    def get_window_default_height_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetWindowDefaultHeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WindowDefaultHeight
                |     parameter.
                |     Role:Retrieves the state of the WindowDefaultHeight parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetWindowDefaultHeightInfo(io_admin_level, io_locked)

    def get_window_default_width_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetWindowDefaultWidthInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WindowDefaultWidth
                |     parameter.
                |     Role:Retrieves the state of the WindowDefaultWidth parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetWindowDefaultWidthInfo(io_admin_level, io_locked)

    def get_window_open_mode_info(self, io_admin_level=None, io_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetWindowOpenModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WindowOpenMode
                |     parameter.
                |     Role:Retrieves the state of the WindowOpenMode parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.sectioning_setting_att.GetWindowOpenModeInfo(io_admin_level, io_locked)

    def set_clipping_mode_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetClippingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClippingMode parameter.
                |     Role:Locks or unlocks the PlaneOrigin parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetClippingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_mode_lock'
        # # vba_code = """
        # # Public Function set_clipping_mode_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetClippingModeLock iLocked
        # #     set_clipping_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_cut_in_wireframe_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDisplayCutInWireframeLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayCutInWireframe parameter.
                |     Role:Locks or unlocks the DisplayCutInWireframe parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetDisplayCutInWireframeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_cut_in_wireframe_lock'
        # # vba_code = """
        # # Public Function set_display_cut_in_wireframe_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetDisplayCutInWireframeLock iLocked
        # #     set_display_cut_in_wireframe_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_auto_filtering_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridAutoFilteringLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridAutoFiltering parameter.
                |     Role:Locks or unlocks the GridAutoFiltering parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridAutoFilteringLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_auto_filtering_lock'
        # # vba_code = """
        # # Public Function set_grid_auto_filtering_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridAutoFilteringLock iLocked
        # #     set_grid_auto_filtering_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_auto_resize_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridAutoResizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridAutoResize parameter.
                |     Role:Locks or unlocks the GridAutoResize parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridAutoResizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_auto_resize_lock'
        # # vba_code = """
        # # Public Function set_grid_auto_resize_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridAutoResizeLock iLocked
        # #     set_grid_auto_resize_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_height_step_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridHeightStepLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridHeightStep parameter.
                |     Role:Locks or unlocks the GridHeightStep parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridHeightStepLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_height_step_lock'
        # # vba_code = """
        # # Public Function set_grid_height_step_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridHeightStepLock iLocked
        # #     set_grid_height_step_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_position_mode_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridPositionModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridPositionMode parameter.
                |     Role:Locks or unlocks the GridPositionMode parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridPositionModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_position_mode_lock'
        # # vba_code = """
        # # Public Function set_grid_position_mode_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridPositionModeLock iLocked
        # #     set_grid_position_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_style_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridStyleLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridStyle parameter.
                |     Role:Locks or unlocks the GridStyle parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridStyleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_style_lock'
        # # vba_code = """
        # # Public Function set_grid_style_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridStyleLock iLocked
        # #     set_grid_style_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_width_step_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetGridWidthStepLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridWidthStep parameter.
                |     Role:Locks or unlocks the GridWidthStep parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetGridWidthStepLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_width_step_lock'
        # # vba_code = """
        # # Public Function set_grid_width_step_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetGridWidthStepLock iLocked
        # #     set_grid_width_step_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_hide_plane_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetHidePlaneLock(boolean iLocked)
                | 
                |     Locks or unlocks the HidePlane parameter.
                |     Role:Locks or unlocks the HidePlane parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetHidePlaneLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_hide_plane_lock'
        # # vba_code = """
        # # Public Function set_hide_plane_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetHidePlaneLock iLocked
        # #     set_hide_plane_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_hide_result_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetHideResultLock(boolean iLocked)
                | 
                |     Locks or unlocks the HideResult parameter.
                |     Role:Locks or unlocks the HideResult parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetHideResultLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_hide_result_lock'
        # # vba_code = """
        # # Public Function set_hide_result_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetHideResultLock iLocked
        # #     set_hide_result_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_plane_color(self, i_r=None, i_g=None, i_b=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the PlaneColor parameter.
                | 
                |     Parameters:
                | 
                |         oR
                |             the red component of the color. 
                |         oG
                |             the green component of the color. 
                |         oB
                |             the blue component of the color.
                | 
                |             Ensure consistency with the C++ interface to which the work is
                |             delegated.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :return: None
        """
        return self.sectioning_setting_att.SetPlaneColor(i_r, i_g, i_b)

    def set_plane_color_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the PlaneColor parameter.
                |     Role:Locks or unlocks the PlaneColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetPlaneColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_plane_color_lock'
        # # vba_code = """
        # # Public Function set_plane_color_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetPlaneColorLock iLocked
        # #     set_plane_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_plane_normal_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneNormalLock(boolean iLocked)
                | 
                |     Locks or unlocks the PlaneNormal parameter.
                |     Role:Locks or unlocks the PlaneNormal parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetPlaneNormalLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_plane_normal_lock'
        # # vba_code = """
        # # Public Function set_plane_normal_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetPlaneNormalLock iLocked
        # #     set_plane_normal_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_plane_origin_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPlaneOriginLock(boolean iLocked)
                | 
                |     Locks or unlocks the PlaneOrigin parameter.
                |     Role:Locks or unlocks the PlaneOrigin parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetPlaneOriginLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_plane_origin_lock'
        # # vba_code = """
        # # Public Function set_plane_origin_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetPlaneOriginLock iLocked
        # #     set_plane_origin_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_section_export_type_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSectionExportTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the SectionExportType parameter.
                |     Role:Locks or unlocks the SectionExportType parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetSectionExportTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_section_export_type_lock'
        # # vba_code = """
        # # Public Function set_section_export_type_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetSectionExportTypeLock iLocked
        # #     set_section_export_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_section_fill_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSectionFillLock(boolean iLocked)
                | 
                |     Locks or unlocks the SectionFill parameter.
                |     Role:Locks or unlocks the SectionFill parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetSectionFillLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_section_fill_lock'
        # # vba_code = """
        # # Public Function set_section_fill_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetSectionFillLock iLocked
        # #     set_section_fill_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_result_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetUpdateResultLock(boolean iLocked)
                | 
                |     Locks or unlocks the UpdateResult parameter.
                |     Role:Locks or unlocks the UpdateResult parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetUpdateResultLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_result_lock'
        # # vba_code = """
        # # Public Function set_update_result_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetUpdateResultLock iLocked
        # #     set_update_result_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viewer_auto_open_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetViewerAutoOpenLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewerAutoOpen parameter.
                |     Role:Locks or unlocks the ViewerAutoOpen parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetViewerAutoOpenLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viewer_auto_open_lock'
        # # vba_code = """
        # # Public Function set_viewer_auto_open_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetViewerAutoOpenLock iLocked
        # #     set_viewer_auto_open_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viewer_auto_reframe_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetViewerAutoReframeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewerAutoReframe parameter.
                |     Role:Locks or unlocks the ViewerAutoReframe parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetViewerAutoReframeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viewer_auto_reframe_lock'
        # # vba_code = """
        # # Public Function set_viewer_auto_reframe_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetViewerAutoReframeLock iLocked
        # #     set_viewer_auto_reframe_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viewer_lock2_d_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetViewerLock2DLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewerLock2D parameter.
                |     Role:Locks or unlocks the ViewerLock2D parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetViewerLock2DLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viewer_lock2_d_lock'
        # # vba_code = """
        # # Public Function set_viewer_lock2_d_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetViewerLock2DLock iLocked
        # #     set_viewer_lock2_d_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_window_default_height_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetWindowDefaultHeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the WindowDefaultHeight parameter.
                |     Role:Locks or unlocks the WindowDefaultHeight parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetWindowDefaultHeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_window_default_height_lock'
        # # vba_code = """
        # # Public Function set_window_default_height_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetWindowDefaultHeightLock iLocked
        # #     set_window_default_height_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_window_default_width_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetWindowDefaultWidthLock(boolean iLocked)
                | 
                |     Locks or unlocks the WindowDefaultWidth parameter.
                |     Role:Locks or unlocks the WindowDefaultWidth parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetWindowDefaultWidthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_window_default_width_lock'
        # # vba_code = """
        # # Public Function set_window_default_width_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetWindowDefaultWidthLock iLocked
        # #     set_window_default_width_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_window_open_mode_lock(self, i_locked=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetWindowOpenModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the WindowOpenMode parameter.
                |     Role:Locks or unlocks the WindowOpenMode parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.sectioning_setting_att.SetWindowOpenModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_window_open_mode_lock'
        # # vba_code = """
        # # Public Function set_window_open_mode_lock(sectioning_setting_att)
        # #     Dim iLocked (2)
        # #     sectioning_setting_att.SetWindowOpenModeLock iLocked
        # #     set_window_open_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SectioningSettingAtt(name="{ self.name }")'