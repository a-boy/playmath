︠905bc964-adca-45a0-886c-39a6e7c7a006s︠
prime_range(100)
︡3039979e-af7c-4f08-973e-d3494bbf170a︡{"stdout":"[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]"}︡{"stdout":"\n"}︡{"done":true}
︠08fa3221-1493-404d-a4bc-51d0c79da7f5s︠
prime_pi(10^6)
︡34ec82cf-0ee4-48f0-9ebc-09bad8aaf88e︡{"stdout":"78498\n"}︡{"done":true}
︠55470366-57c0-40d9-afb9-90a5c3762b6ds︠
factor(2^1277-1)
︡81f717d1-2b30-4811-949b-d2155ae80302︡{"stderr":"<string>:1: RuntimeWarning: cypari2 leaked 2392440 bytes on the PARI stack\n"}︡{"stderr":"Error in lines 1-1\nTraceback (most recent call last):\n  File \"/cocalc/lib/python2.7/site-packages/smc_sagews/sage_server.py\", line 1188, in execute\n    flags=compile_flags), namespace, locals)\n  File \"\", line 1, in <module>\n  File \"/ext/sage/sage-8.8_1804/local/lib/python2.7/site-packages/sage/arith/misc.py\", line 2594, in factor\n    verbose=verbose, **kwds)\n  File \"sage/rings/integer.pyx\", line 3931, in sage.rings.integer.Integer.factor (build/cythonized/sage/rings/integer.c:24830)\n    F = factor_using_pari(n, int_=int_, debug_level=verbose, proof=proof)\n  File \"sage/rings/factorint.pyx\", line 345, in sage.rings.factorint.factor_using_pari (build/cythonized/sage/rings/factorint.c:6392)\n    p, e = n.__pari__().factor(proof=proof)\n  File \"cypari2/gen.pyx\", line 4307, in cypari2.gen.Gen.factor\nKeyboardInterrupt\n"}︡{"done":true}
︠3e2fa98f-712b-4122-9699-e37e63225462s︠
graphs.PetersenGraph().plot()
︡1ddd2723-2991-404a-adaa-f0389bb01ce9︡{"file":{"filename":"/home/user/.sage/temp/project-2f326863-5026-4b6e-8677-cd9b9c781d91/515/tmp_1LAdH_.svg","show":true,"text":null,"uuid":"aeb3a957-fa41-4a09-bb5f-9ac2f72afda1"},"once":false}︡{"done":true}
