#! /usr/local/bin/python3

print ('Content-type:text/html \n')


text = """ <!DOCTYPE HTML>

<html>
      <head>
             <title>Python CGI</title>

      </head>

  <body LINK="#ff8080" VLINK="#ff0000" ALINK="a05050" STYLE="background: #000000; color: #80c0c0">
  <h1 ALIGN="center" STYLE="background: #000080; font: 36pt/40pt courier; font-variant: small-caps; border: thick dashed blue">Welcome to my home page!</h1>
      <br><br>
  <p><span STYLE="margin-left: 25px">Hi there! If you are reading this then you have found $text Congratulations!</span>
      I know it can be hard to find my pages, but I bet that you feel lucky now. Now that you are here, please take a look at my page of links to <a HREF="http://www.mysite.com/coolsites.html">cool sites</a> or sign my <a HREF="http://www.mysite.com/guestbook.html">guest book</a></p>
  <div><div STYLE="font-weight: bold; margin-left: 30px">
 <span STYLE="font-size: x-large; color: #ffffff">M</span>y wonderful poetry</div> is available if you are REALLY bored. Why not give it a spin?</div>

  <h2 STYLE="background: #000080; color: green; line-height: 50px; font-size: 40px">
  The Best Poetry I <em STYLE="font-weight: 900">NEVER</em> Wrote</h2>
      <ul>
         <li>'There Once Was A Man From Nantucket' -
               <span STYLE="font-family: 'comic sans ms', fantasy; color: rgb(100%, 100%, 0%)">Anonymous</span></li>
          <li>'Cool In Fur' -
               <span STYLE="font-family: 'comic sans ms', fantasy; color: rgb(100%, 100%, 0%)">Harry B. Foot</span></li>
          <li>And My All Time Fave:
           <ul>
           <li STYLE="font-size: x-large; font-style: italic"> 'A Toast To My Toaster' -
               <span STYLE="font-family: 'comic sans ms', fantasy; color: rgb(100%, 100%, 0%)">Me!</span></li>
           </ul>
      </li></ul>

  <blockquote STYLE="background: #000080; color: #00ff00; margin-left: 2cm">Brought to you by the letter
  <span STYLE="font-family: 'comic sans ms', fantasy; color: rgb(100%, 100%, 0%)">&quot;H&quot;</span>
  and <span STYLE="Padding: 20px; border: 20px groove #ffffff">Joe Public</span> </blockquote>

  <div STYLE="background: #000080; font-weight: bold; margin-left: 30px">
  <span STYLE=""font-size: x-large; color: #ffffff"> W</span>hen you are done looking through these masterpieces, I encourage you to visit my proud sponsor!! </div>

  <p STYLE="font: 12pt/14pt sans-serif; margin: 5px 0px 2px 25px; border: medium dashed #ff0000; background: white url(http://www.foo.com/image.gif) repeat-x fixed top right }">
  <span STYLE="font: 36pt/40pt courier; font-variant: small-caps; border: thick dashed blue }"> ADVERTISEMENT:</span>
      Buy Navel Lint Contemplator! Its a browser and its a sandwich spread! Go to our <a HREF="http://www.navellint.com">home page</a> without delay! Why? Because shelf life is only 8 hours unless refrigerated. We know that makes it hard to browse, but it promotes frequent upgrading to the latest and greatest version. </p>



      </body>
      </html>

"""
print(text)
