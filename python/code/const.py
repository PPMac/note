#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1、使用__setattr__来控制重新绑定
2、sys.modules[name]得到的是模块对象，通过模块对象可以访问其模块属性；
而Python不会进行严格的类型检测，所以直接将一个 _const类对象加入sys.modules字典，
而__name__的值为对应模块const的名字const，通过 sys.modules[__name__] = _const()用类对象替换模块对象，将对应的名字空间加以限制.
当使用import const时，会发生sys.modules[const] = _const()；
而访问const.attrvalue时会发生sys.modules[const].attrvalue，即 _const().attrvalue
"""

#以单下划线开头的变量和函数被默认当作内部函数，如果使用 from a_module import * 导入时，这部分变量和函数不会被导入
class _const:

    class _ConstTypeError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self._ConstTypeError, "Can't rebind const %s" % name
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self._ConstTypeError, "Can't unbind const %s" % name

import sys
sys.modules[__name__] = _const()
