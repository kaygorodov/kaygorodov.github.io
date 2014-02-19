Достаточно долго, провозился с дебагом ангулар приложения, пока не выяснил, что используя $cookies, можно выставлять только строки:

<div class="highlight">
<pre>
$cookies.token = 222; // кука не выставится
console.log($cookies.token) // undefined
$cookies.token = "222"; // кука выставится
</pre>
</div>