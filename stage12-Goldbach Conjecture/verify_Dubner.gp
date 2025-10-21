\\ pari/gp script: search for even d with ji +/- d both twin primes
\\ Assumptions:
\\ - "first n twin primes" = the first n twin pairs; we take the smaller member of each pair
\\ - d is even
\\ - require ji > 2*10^10 (if not, we increment n until it is)
\\ - require ji - d > nth_twin_prime (the smaller member of the nth pair)

\\ default(maxprimelimit, 10^7); \\ safety for before 2.18 version

is_twinprime(p) = {
  if(p<2, return(0));
  if(!isprime(p), return(0));
  return(isprime(p+2) || (p>2 && isprime(p-2)));
}

first_n_twin_lowers(n) = {
  local(list = vector(n));
  k = 3; i = 1;
  while(i <= n,
    if(isprime(k) && isprime(k+2),
      list[i] = k; i++;
    );
    k += 2;
  );
  return(list);
}

check_range(nmin, nmax, maxD=10^6) = {
  for(n=nmin, nmax,
    lowers = first_n_twin_lowers(n);
    ji = 1;
    for(i=1, #lowers, ji *= lowers[i]);
    print("n = ", n, " --> ji has ", length(Str(ji)), " digits");
    if(ji <= 2*10^10, print("  (skip: ji <= 2*10^10)"); next);
    nth_lower = lowers[n];
    maxD_eff = min(maxD, ji - nth_lower - 1);
    if(maxD_eff < 2, print("  (skip: ji - nth_lower <= 2)"); next);

    found = 0;
    for(d=2, maxD_eff,
      if(d % 2, next); \\ even d only
      a = ji + d;
      b = ji - d;
      if(is_twinprime(a) && is_twinprime(b),
        print("  FOUND for n=", n, ": d=", d);
        print("    ji - d = ", b);
        print("    ji + d = ", a);
        found = 1; break;
      );
    );
    if(!found, print("  no d found up to ", maxD_eff));
  );
}

\\ Example run for n=20..25, search up to 1e6:
\\ check_range(6, 15, 10^7);
\\ check_range(16, 20, 10^7);
\\ check_range(21, 25, 10^7);
check_range(26, 30, 10^7);