# utils.py

# A place where fugly code goes ;).

import json
import asyncio
import datetime

# For ThreadWithExc.
import time
import ctypes
import inspect
import threading


class ThreadWithExc(threading.Thread):
    """Thread with a terminate.

    A thread class that supports raising an exception in the thread from
    another thread.

    http://tomerfiliba.com/recipes/Thread2/\

    """
    def __get_my_tid(self):
        """determines this (self's) thread id

        CAREFUL: this function is executed in the context of the caller
        thread, to get the identity of the thread represented by this
        instance.

        """
        if not self.is_alive():
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        raise AssertionError("could not determine the thread's id")

    def raiseExc(self, exctype):
        """Raises the given exception type in the context of this thread.

        If the thread is busy in a system call (time.sleep(),
        socket.accept(), ...), the exception is simply ignored.

        If you are sure that your exception should terminate the thread,
        one way to ensure that it works is:

            t = ThreadWithExc( ... )
            ...
            t.raiseExc( SomeException )
            while t.isAlive():
                time.sleep( 0.1 )
                t.raiseExc( SomeException )

        If the exception is to be caught by the thread, you need a way to
        check that your thread has caught it.

        CAREFUL: this function is executed in the context of the
        caller thread, to raise an exception in the context of the
        thread represented by this instance.

        """
        self.__async_raise( self.__get_my_tid(), exctype )

	# This raises an exception in the threads with id tid.
    @staticmethod
    def __async_raise(tid, exctype):
        
        if not inspect.isclass(exctype):
            raise TypeError("Only types can be raised (not instances)")

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        	ctypes.c_long(tid), 
        	ctypes.py_object(exctype))

        if res == 0:
            raise ValueError("invalid thread id")

        elif res != 1:

            # "if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), 
                None)

            raise SystemError("PyThreadState_SetAsyncExc failed")
