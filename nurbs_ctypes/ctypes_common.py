import ctypes
from ctypes import POINTER, Structure


# TODO
class Library(Structure):
    """
        typedef struct Library {
      ID id;
      struct FileData *filedata;
      /** Path name used for reading, can be relative and edited in the outliner. */
      char name[1024];

      /**
       * Absolute filepath, this is only for convenience,
       * 'name' is the real path used on file read but in
       * some cases its useful to access the absolute one.
       * This is set on file read.
       * Use BKE_library_filepath_set() rather than setting 'name'
       * directly and it will be kept in sync - campbell */
      char filepath[1024];

      /** Set for indirectly linked libs, used in the outliner and while reading. */
      struct Library *parent;

      struct PackedFile *packedfile;

      /* Temp data needed by read/write code. */
      int temp_index;
      /** See BLENDER_VERSION, BLENDER_SUBVERSION, needed for do_versions. */
      short versionfile, subversionfile;
    } Library;
    """
    pass


# TODO
class ID(Structure):
    """
    typedef struct ID {
      void *next, *prev;
      struct ID *newid;
      struct Library *lib;
      /** MAX_ID_NAME. */
      char name[66];
      /**
       * LIB_... flags report on status of the data-block this ID belongs to
       * (persistent, saved to and read from .blend).
       */
      short flag;
      /**
       * LIB_TAG_... tags (runtime only, cleared at read time).
       */
      int tag;
      int us;
      int icon_id;
      int recalc;
      char _pad[4];
      IDProperty *properties;

      /** Reference linked ID which this one overrides. */
      IDOverrideLibrary *override_library;

      /**
       * Only set for data-blocks which are coming from copy-on-write, points to
       * the original version of it.
       */
      struct ID *orig_id;

      void *py_instance;
    } ID;"""
    pass
