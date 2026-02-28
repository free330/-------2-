# utils/event_dispatcher.py
class EventDispatcher:
    """简单的事件分发器，支持注册监听器和触发事件"""
    def __init__(self):
        self._listeners = {}

    def register(self, event_type, callback):
        """注册事件监听器
        :param event_type: 事件类型（字符串）
        :param callback: 回调函数，接受一个data参数
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unregister(self, event_type, callback):
        """移除监听器"""
        if event_type in self._listeners:
            self._listeners[event_type].remove(callback)

    def dispatch(self, event_type, data=None):
        """触发事件，通知所有监听器"""
        if event_type in self._listeners:
            for callback in self._listeners[event_type]:
                callback(data)