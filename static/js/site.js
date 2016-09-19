function GetPasswords()
{
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/pwd/get/' + document.getElementById('url').value, false);
  xhr.send();

  if (xhr.status == 200)
  {
    pwd_data = JSON.parse(xhr.responseText);

    function JsonLength(obj)
    {
      var count = 0
      for (var item in obj)
      {
        count++;
      }
      return count;
    }

    // очищаем div с контентом
    document.getElementById('pwd').innerHTML = '';

    for (var i = 0; i < JsonLength(pwd_data); i++)
    {
      // alert(pwd_data[i]['url']);
      var newItem = document.createElement('div');
      newItem.className = 'item';
      newItem.innerHTML = '<p class="item-url">'+pwd_data[i]['url']+'</p>\
        <input class="item-email" value="'+pwd_data[i]['email']+'"><!--\
      --><input class="item-login" value="'+pwd_data[i]['login']+'">\
        <input id="'+i+'" type="password" class="item-pass" value="'+pwd_data[i]['pass']+'"><!--\
      --><button class="item-pwd-show" onclick="ShowPassword('+i+');">@</button>';
      document.getElementById('pwd').appendChild(newItem);
    }
  }
}

function ShowPassword(pwd_id)
{
  if (document.getElementById(pwd_id).type == 'password')
  {
    document.getElementById(pwd_id).type = 'text';
  }
  else
  {
    document.getElementById(pwd_id).type = 'password';
  }
}
