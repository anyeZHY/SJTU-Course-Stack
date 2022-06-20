% >>>> Preprocess >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
origin = im2double(imread('baboon.bmp'));

% Blurred image
PSF = ones([5,5])*0.04;
% blurred = conv2(origin,PSF);
% size = 516;
blurred = conv2(origin,PSF,'same');
size = 512;

% Blurred and noised image
bn30 = awgn(blurred,30,'measured');
bn20 = awgn(blurred,20,'measured');
bn10 = awgn(blurred,10,'measured');
% <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


% >>>> Filtering >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
% Implement filtering directly
% F_SPF = fft2(PSF,size,size);
% r1 = ifft2(fft2(bn10)./F_SPF);
% r2 = ifft2(fft2(bn20)./F_SPF);
% r3 = ifft2(fft2(bn30)./F_SPF);
% For simplicity, we could use deconvwnr(bn, PSF)
df1 = deconvwnr(bn10, PSF);
df2 = deconvwnr(bn20, PSF);
df3 = deconvwnr(bn30, PSF);
% Implement wiener filtering
wnr1 = deconvwnr(bn10, PSF, 0.1);
wnr2 = deconvwnr(bn20, PSF, 0.01);
wnr3 = deconvwnr(bn30, PSF, 0.001);
% Save them
imwrite(blurred,"blurred.bmp")
imwrite(bn10,"bn1.bmp")
imwrite(bn20,"bn2.bmp")
imwrite(bn30,"bn3.bmp")
imwrite(df1,"df1.bmp")
imwrite(df2,"df2.bmp")
imwrite(df3,"df3.bmp")
imwrite(wnr1,"wnr1.bmp")
imwrite(wnr2,"wnr2.bmp")
imwrite(wnr3,"wnr3.bmp")
% <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


% implement pseudo-inverse filtering
% Here \epsilon = 0.5
% 
% F_PSF = fft2(PSF,size,size);
% H = (abs(F_PSF)>0.5)./F_PSF;
% F_bn30 = fft2(bn30);
% F_bn20 = fft2(bn20);
% F_bn10 = fft2(bn10);
% rr1 = ifft2(F_bn10.*H);
% rr2 = ifft2(F_bn20.*H);
% rr3 = ifft2(F_bn30.*H);