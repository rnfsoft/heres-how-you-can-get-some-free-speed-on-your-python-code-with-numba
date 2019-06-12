Tutorial from:
https://towardsdatascience.com/heres-how-you-can-get-some-free-speed-on-your-python-code-with-numba-89fdc8249ef3

test1.py
    Without
        Average time = 0.04226064205169678

    With
        warnings.warn(NumbaPendingDeprecationWarning(msg, loc=loc))
        Average time = 0.20426002502441407

test2.py
    Without 
        Average time = 0.0160208797454834
    With
        Average time = 0.002759981155395508
