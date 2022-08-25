# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-08
Description :
auther : wcy
"""
# import modules

__all__ = []


# define class
class object:
    """
    The base class of the class hierarchy.

    When called, it accepts no arguments and returns a new featureless
    instance that has no instance attributes and cannot be given any.
    """

    def __delattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement delattr(self, name). """
        """
        Deletes the named attribute from the given object.
        delattr(x, 'y') is equivalent to ``del x.y''
        """
        pass

    def __dir__(self, *args, **kwargs):  # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs):  # real signature unknown
        """
        This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self):  # known special case of object.__init__
        """ Initialize self.  See help(type(self)) for accurate signature. """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(cls, *more):  # known special case of object.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        pass

    @classmethod  # known case
    def __subclasshook__(cls, subclass):  # known special case of object.__subclasshook__
        """
        Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    __class__ = None  # (!) forward: type, real value is ''
    __dict__ = {}
    __doc__ = ''
    __module__ = ''
