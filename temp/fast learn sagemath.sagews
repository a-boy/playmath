︠905bc964-adca-45a0-886c-39a6e7c7a006s︠
prime_range(100)
︡3039979e-af7c-4f08-973e-d3494bbf170a︡{"stdout":"[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]"}︡{"stdout":"\n"}︡{"done":true}
︠08fa3221-1493-404d-a4bc-51d0c79da7f5s︠
prime_pi(10^6)
︡34ec82cf-0ee4-48f0-9ebc-09bad8aaf88e︡{"stdout":"78498\n"}︡{"done":true}
︠55470366-57c0-40d9-afb9-90a5c3762b6ds︠
factor(2^97-1)
︡8c3e2fdf-c09d-463f-b11c-de49a22c952a︡{"stdout":"11447 * 13842607235828485645766393\n"}︡{"done":true}
︠3e2fa98f-712b-4122-9699-e37e63225462s︠
graphs.PetersenGraph().plot()
︡1ddd2723-2991-404a-adaa-f0389bb01ce9︡{"file":{"filename":"/home/user/.sage/temp/project-2f326863-5026-4b6e-8677-cd9b9c781d91/515/tmp_1LAdH_.svg","show":true,"text":null,"uuid":"aeb3a957-fa41-4a09-bb5f-9ac2f72afda1"},"once":false}︡{"done":true}
︠cfd511fd-000a-4c97-a366-c9abe0b28a40s︠
f1 = 1
f2 = 1-x
f3 = exp(x)
f4 = sin(2*x)
f = piecewise([((0,1),f1), ((1,2),f2), ((2,3),f3), ((3,10),f4)])
f.plot(x,0,10)
︡807d153b-dda8-44ce-8f5b-47668528ccf9︡{"file":{"filename":"/home/user/.sage/temp/project-2f326863-5026-4b6e-8677-cd9b9c781d91/1820/tmp_7fwsf8dh.svg","show":true,"text":null,"uuid":"33ca467c-1262-4705-b12e-4da86c4ac1ed"},"once":false}︡{"done":true}
︠a488750f-328d-4324-ba61-ec197f34e044s︠
L = [(i/100.0, maxima.eval('jacobi_sn (%s/100.0,2.0)'%i))
    for i in range(-300,300)]
show(line(L, rgbcolor=(3/4,1/4,1/8)))
︡b34ba9b1-a6d8-45b2-905c-80be79c542c9︡{"file":{"filename":"/home/user/.sage/temp/project-2f326863-5026-4b6e-8677-cd9b9c781d91/1820/tmp_wdenhb46.svg","show":true,"text":null,"uuid":"431eda61-f1ff-4007-b0e3-614170bdbafb"},"once":false}︡{"done":true}
︠18360f5c-5862-47ff-b9ad-17f99ac04961s︠
I = CDF.0
show(line([zeta(1/2 + k*I/6) for k in range(180)], rgbcolor=(3/4,1/2,5/8)))
︡0659bb92-9c27-4236-8e15-84a280240573︡{"file":{"filename":"/home/user/.sage/temp/project-2f326863-5026-4b6e-8677-cd9b9c781d91/1820/tmp_ay0s01do.svg","show":true,"text":null,"uuid":"36106951-b5ef-4965-b225-a229bc722885"},"once":false}︡{"done":true}
︠983aebce-47c5-4394-92a8-049006407c36s︠
var('x k w')
f = x^3 * e^(k*x) * sin(w*x)
show(f)
print("Differentiate f w.r.t. x")
show(f.diff(x))
︡9e984dc8-f523-4c7a-a7ee-454e4dde560a︡{"stdout":"(x, k, w)"}︡{"stdout":"\n"}︡{"html":"<div align='center'>$\\displaystyle x^{3} e^{\\left(k x\\right)} \\sin\\left(w x\\right)$</div>"}︡{"stdout":"Differentiate f w.r.t. x\n"}︡{"html":"<div align='center'>$\\displaystyle w x^{3} \\cos\\left(w x\\right) e^{\\left(k x\\right)} + k x^{3} e^{\\left(k x\\right)} \\sin\\left(w x\\right) + 3 \\, x^{2} e^{\\left(k x\\right)} \\sin\\left(w x\\right)$</div>"}︡{"done":true}
︠716e415c-4acd-4b62-a2f6-4efff0f3c607︠
 Partitions(10).










