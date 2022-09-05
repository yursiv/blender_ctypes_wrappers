import ctypes
from ctypes import POINTER, Structure


class BezTriple(Structure):
    """
    typedef struct BezTriple {
      float vec[3][3];
      float tilt;
      float weight;
      float radius;
      char ipo;
      char h1, h2;
      char f1, f2, f3;
      char hide;
      char easing;
      float back;
      float amplitude, period;
      char f5;
      char _pad[3];
    } BezTriple;
    """

    _fields_ = [
        ("vec", ctypes.c_float * 3 * 3),

        ("tilt", ctypes.c_float),
        ("weight", ctypes.c_float),
        ("radius", ctypes.c_float),

        ("ipo", ctypes.c_char),

        ("h1", ctypes.c_char),
        ("h2", ctypes.c_char),

        ("f1", ctypes.c_char),
        ("f2", ctypes.c_char),
        ("f3", ctypes.c_char),

        ("hide", ctypes.c_char),

        ("easing", ctypes.c_char),

        ("back", ctypes.c_float),
        ("amplitude", ctypes.c_float),
        ("period", ctypes.c_float),

        ("f5", ctypes.c_char),
        ("_pad", ctypes.c_char * 3),
    ]


class BPoint(Structure):
    """
    typedef struct BPoint {
      float vec[4];
      float tilt;
      float weight;
      short f1, hide;
      float radius;
      char _pad[4];
    } BPoint;
    """
    _fields_ = [
        ("vec", ctypes.c_float * 4),

        ("tilt", ctypes.c_float),
        ("weight", ctypes.c_float),

        ("f1", ctypes.c_short),
        ("hide", ctypes.c_short),

        ("radius", ctypes.c_float),
        ("_pad", ctypes.c_char * 4),
    ]


class Nurb(Structure):
    """
    \source\blender\makesdna\DNA_curve_types.h

    typedef struct Nurb {
      struct Nurb *next, *prev;
      short type;
      short mat_nr;
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
    } Nurb;"""

    pass


Nurb._fields_ = [
    ("next", POINTER(Nurb)),
    ("prev", POINTER(Nurb)),

    ("type", ctypes.c_short),

    ("mat_nr", ctypes.c_short),
    ("hide", ctypes.c_short),
    ("flag", ctypes.c_short),

    ("pntsu", ctypes.c_int),
    ("pntsv", ctypes.c_int),

    ("_pad", ctypes.c_char * 4),

    ("resolu", ctypes.c_short),
    ("resolv", ctypes.c_short),
    ("orderu", ctypes.c_short),
    ("orderv", ctypes.c_short),
    ("flagu", ctypes.c_short),
    ("flagv", ctypes.c_short),

    ("knotsu", POINTER(ctypes.c_float)),
    ("knotsv", POINTER(ctypes.c_float)),

    ("bp", POINTER(BPoint)),
    ("bezt", POINTER(BezTriple)),

    ("tilt_interp", ctypes.c_short),
    ("radius_interp", ctypes.c_short),

    ("charidx", ctypes.c_int),
]

#TODO

class Curve(Structure):
    """
    typedef struct Curve {
      ID id;
      /** Animation data (must be immediately after id for utilities to use it). */
      struct AnimData *adt;

      /** Actual data, called splines in rna. */
      ListBase nurb;

      /** Edited data, not in file, use pointer so we can check for it. */
      EditNurb *editnurb;

      struct Object *bevobj, *taperobj, *textoncurve;
      /** Old animation system, deprecated for 2.5. */
      struct Ipo *ipo DNA_DEPRECATED;
      struct Key *key;
      struct Material **mat;

      /* texture space, copied as one block in editobject.c */
      float loc[3];
      float size[3];

      /** Creation-time type of curve datablock. */
      short type;

      /** Keep a short because of BKE_object_obdata_texspace_get(). */
      short texflag;
      char _pad0[6];
      short twist_mode;
      float twist_smooth, smallcaps_scale;

      int pathlen;
      short bevresol, totcol;
      int flag;
      float width, ext1, ext2;

      /* default */
      short resolu, resolv;
      short resolu_ren, resolv_ren;

      /* edit, index in nurb list */
      int actnu;
      /* edit, index in active nurb (BPoint or BezTriple) */
      int actvert;

      char overflow;
      char spacemode, align_y;
      char _pad[3];

      /* font part */
      short lines;
      float spacing, linedist, shear, fsize, wordspace, ulpos, ulheight;
      float xof, yof;
      float linewidth;

      /* copy of EditFont vars (wchar_t aligned),
       * warning! don't use in editmode (storage only) */
      int pos;
      int selstart, selend;

      /* text data */
      /** Number of characters (strinfo). */
      int len_wchar;
      /** Number of bytes (str - utf8). */
      int len;
      char *str;
      struct EditFont *editfont;

      char family[64];
      struct VFont *vfont;
      struct VFont *vfontb;
      struct VFont *vfonti;
      struct VFont *vfontbi;

      struct TextBox *tb;
      int totbox, actbox;

      struct CharInfo *strinfo;
      struct CharInfo curinfo;
      /* font part end */

      /** Current evaltime - for use by Objects parented to curves. */
      float ctime;
      float bevfac1, bevfac2;
      char bevfac1_mapping, bevfac2_mapping;

      char _pad2[6];
      float fsize_realtime;

      void *batch_cache;
    } Curve;
    """





"""
import bpy

spline_ptr = bpy.context.object.data.splines[0].as_pointer()
pnt_ptr = bpy.context.object.data.splines[0].points[0].as_pointer()

# p = POINTER(Nurb)(Nurb.from_address(spline_ptr))
c_spline_ptr = ctypes.cast(spline_ptr, POINTER(Nurb))
c_pnt_ptr = ctypes.cast(pnt_ptr, POINTER(BPoint))

# print(c_spline_ptr.contents.__dir__())
cp(c_spline_ptr.contents.pntsu)
# cp(c_pnt_ptr.contents.weight)
knots = c_spline_ptr.contents.knotsu
cp(knots.value)
"""
