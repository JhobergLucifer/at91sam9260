%Jhoberg 
%Engineer
%Division Polinomio Convolucion

function [q,r,qc,rc] = polydiv_conv(b,a,c)
% Polynomial division by convolution.
n = length(b);
m = length(a);
if m > n, 
  q = 0; 
  r = b; 
  qc = 0; 
  rc = b; 
  c = 1; 
  return; 
end;
if nargin < 3, 
  c == 1; 
end;
w(1) = 1;
 if c == 0, 
  w(1) = a(1)^(n-m+1); 
 end;
for k = 2:n-m+2,
w(k) = [b(k-1),-a(min(k-1,m):-1:2)]*[w(1),w(max(2,k+1-m):k-1)]'/a(1);
end
for k = n-m+3:n+1,
w(k) = [b(k-1),-a(min(m,k-1):-1:k-1+m-n)]*[w(1),w(max(k+1-m,2):n-m+2)]';
end;
c = w(1);
qc = w(2:n-m+2);
rc = w(n-m+3:n+1);
q = qc/c;
r = rc(min(find(abs(rc)>0)):end)/c;

