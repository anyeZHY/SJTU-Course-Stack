% Initialization
orig = double(imread("roman.jpg"))/255;
gray = orig(:,:,1);


%% ===== Problem 1, 2 and 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
gray1 = histeq(gray);
mean_gray = mean(gray, "all");

exp = exprnd(0.6,900,1440);
[exp, ] = imhist(exp, 66);
exp = exp(2:65);
gray2 = histeq(gray, exp);

gau = normrnd(0.5, 0.24, 900, 1440);
[gau, ] = imhist(gau, 66);
gau = gau(2:65);
gray3 = histeq(gray, gau);

beta = betarnd(2, 2, 900, 1440);
[beta, ] = imhist(beta, 66);
beta = beta(2:65);
gray4 = histeq(gray, beta);

gam = gamrnd(1.2, 2, 900, 1440);
[gam, ] = imhist(gam, 66);
gam = gam(2:65);
gray5 = histeq(gray, gam);


%% ===== Problem 4 and 5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
% naive version
enhanced1 = zeros(900, 1440, 3);
for i = (1:3)
    channel = orig(:,:,i);
    enhanced1(:,:,i) = histeq(channel);
end
% gaussian distribution
gau = normrnd(0.5, 0.3, 900, 1440);
[gau, ] = imhist(gau, 66);
gau = gau(2:65);
enhanced2 = zeros(900, 1440, 3);
for i = (1:3)
    channel = orig(:,:,i);
    enhanced2(:,:,i) = histeq(channel, gau);
end
% Contrast-limited adaptive
enhanced3 = zeros(900, 1440, 3);
for i = (1:3)
    channel = orig(:,:,i);
    enhanced3(:,:,i) = adapthisteq(channel);
end
% Gamma
enhanced4 = (orig).^(1/2);

figure()
subplot(2,2,1)
imshow(enhanced1)
title('Enhanced (naive)')
subplot(2,2,2)
imshow(enhanced2)
title('Gaussian')
subplot(2,2,3)
imshow(enhanced3)
title('Contrast-limited adaptive')
subplot(2,2,4)
imshow(enhanced4)
title('Gamma Correction')

%% ===== Visualization >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
figure("Name","Comparation")

subplot(3,2,1)
imshow(gray)
title('Original')

subplot(3,2,2)
imshow(gray1)
title('Equalization')

subplot(3,2,3)
imshow(gray2)
title('Exponential')

subplot(3,2,4)
imshow(gray3)
title('Gaussian')

subplot(3,2,5)
imshow(gray4)
title('Beta')

subplot(3,2,6)
imshow(gray5)
title('Gamma')