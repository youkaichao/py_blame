import torch

import sys
found = False
import traceback

def _trace_calls(frame, event, arg=None):
    if event in ['call', 'return']:
        # for every function call or return
        try:
            global found
            # Temporarily disable the trace function
            sys.settrace(None)
            # check condition here
            if not found and torch.cuda.device_count.cache_info().currsize > 0:
            # if not found and torch.cuda._initialized:
                found = True
                traceback.print_stack()
            # Re-enable the trace function
            sys.settrace(_trace_calls)
        except NameError:
            # modules are deleted during shutdown
            pass
    return _trace_calls
sys.settrace(_trace_calls)
