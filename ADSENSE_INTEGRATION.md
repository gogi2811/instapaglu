# Google AdSense Integration Guide

This guide provides step-by-step instructions on how to integrate Google AdSense into your website to display ads and earn revenue.

## What is Google AdSense?

Google AdSense is a program run by Google that allows website owners (publishers) to display targeted ads on their websites. You earn money when visitors see or interact with these ads.

## Step-by-Step Integration Guide

### Step 1: Sign Up for Google AdSense
1.  Go to the [Google AdSense website](https://www.google.com/adsense/start/).
2.  Click on "Get Started" and sign up with your Google account.
3.  Provide your website URL (e.g., `http://www.instapaglu.com`) and your payment information.

### Step 2: Get Your Website Approved
-   After you sign up, Google will review your website to ensure it complies with their program policies. This process can take from a few days to a couple of weeks.
-   Make sure your website has unique content and a good user experience to increase your chances of approval.

### Step 3: Create an Ad Unit
1.  Once your AdSense account is approved, log in to your dashboard.
2.  Navigate to the "Ads" section.
3.  Click on "By ad unit" and choose the type of ad you want to create (e.g., "Display ads").
4.  Select the size and shape of your ad (e.g., a responsive ad, a fixed-size banner).
5.  Give your ad unit a name and click "Create".

### Step 4: Place the Ad Code on Your Website
1.  After creating the ad unit, AdSense will provide you with a snippet of JavaScript code.
2.  Copy this code.
3.  Open the `public/index.html` file in your project.
4.  Find the section marked as `<!-- Google Ads Placeholder -->`.
5.  Replace the placeholder `div` with the AdSense code you copied.

**Example:**

Replace this placeholder:
```html
<!-- Google Ads Placeholder -->
<div class="my-6 border-t border-gray-200 pt-4">
  <div class="bg-gray-200 w-full h-24 flex items-center justify-center">
    <span class="text-gray-500 text-sm">Ad Placeholder</span>
  </div>
</div>
```

With your AdSense code, which will look something like this (this is just an example):
```html
<!-- Google Ads Placeholder -->
<div class="my-6 border-t border-gray-200 pt-4">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-your-publisher-id"
     crossorigin="anonymous"></script>
  <!-- Your Ad Unit Name -->
  <ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-your-publisher-id"
     data-ad-slot="your-ad-slot-id"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
  <script>
     (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>
```

Once you have placed the code, Google will start serving ads on your website, and you can monitor your earnings from your AdSense dashboard.
