from ctypes import POINTER, cast

from .ctypes_ import Nurb, BPoint


class CP:
    def __init__(self, cp):
        self.ptr = cp.as_pointer()
        self.c_ptr = cast(self.ptr, POINTER(BPoint))


class NurbsSpline:
    def __init__(self, spline):
        self.ptr = spline.as_pointer()
        self.c_ptr = cast(self.ptr, POINTER(Nurb))

    @property
    def type(self):
        t = self.c_ptr.contents.type
        if t == 0:
            return "POLY"

        elif t == 1:
            return "BEZIER"

        elif t == 4:
            return "NURBS"

        return None

    @property
    def hide(self):
        return self.c_ptr.contents.hide

    @property
    def flag(self):
        return self.c_ptr.contents.flag

    @property
    def mat_nr(self):
        return self.c_ptr.contents.mat_nr

    @property
    def pntsu(self):
        return self.c_ptr.contents.pntsu

    @property
    def pntsv(self):
        return self.c_ptr.contents.pntsv

    @property
    def pad(self):
        return self.c_ptr.contents._pad

    @property
    def resolu(self):
        return self.c_ptr.contents.resolu

    @property
    def resolv(self):
        return self.c_ptr.contents.resolv

    @property
    def orderu(self):
        return self.c_ptr.contents.orderu

    @property
    def orderv(self):
        return self.c_ptr.contents.orderv

    @property
    def flagu(self):
        return self.c_ptr.contents.flagu

    @property
    def flagv(self):
        return self.c_ptr.contents.flagv

    @property
    def knotsu(self):
        knotsu = self.c_ptr.contents.knotsu
        return [knotsu[i] for i in range(self.pntsu + self.orderu)]

    @property
    def knotsv(self):
        knotsv = self.c_ptr.contents.knotsv
        return [knotsv[i] for i in range(self.pntsv + self.orderv)]

    @property
    def tilt_interp(self):
        return self.c_ptr.contents.tilt_interp

    @property
    def radius_interp(self):
        return self.c_ptr.contents.radius_interp

    @property
    def charidx(self):
        return self.c_ptr.contents.charidx


    """"
     short hide, flag;
      int pntsu, pntsv;
      char _pad[4];
      short resolu, resolv;
      short orderu, orderv;
      short flagu, flagv;

      float *knotsu, *knotsv;
      BPoint *bp;
      BezTriple *bezt;

      short tilt_interp;
      short radius_interp;

      int charidx;
    
    """
