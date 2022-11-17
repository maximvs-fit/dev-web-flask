function testeBotao2() {
  setTimeout(() => {
    document.getElementById("message").value =
      "preenchendo o valor do textarea!!!";
  }, 3000);
}

const entrada = document.getElementById("message");

// console.log("objeto do input", entrada);

async function testeAsync() {
  // throw new Error("deu ruim!");
  await new Promise((r) => setTimeout(r, 3000));
  return 10;
}

async function testeAsync2() {
  console.log("iniciou teste 2");
  testeAsync()
    .then((t) => console.log(t))
    .catch((erro) => console.log(erro))
    .finally(() => console.log("fim 2"));
  console.log("vai logar imediatamente depois de chamar a função testeAsync");
}

async function testeAsync3() {
  console.log("iniciou teste 3");
  try {
    const resposta = await testeAsync();
    console.log(resposta);
  } catch (erro) {
    console.log(erro);
  } finally {
    console.log("fim 3");
  }
  console.log(
    "só vai logar depois de encerrada a execução da função testeAsync"
  );
}

function testeAjax() {
  const user = {
    nome: "Rafael",
    email: "rafael@teste.com",
    turmas: ["ads 2c", "gti 2a"],
  };

  console.log("objeto inicial", user);

  const valorJson = JSON.stringify(user);
  console.log("json do usuário", valorJson);

  const valorProcessado = JSON.parse(valorJson);
  console.log("json processado a partir da string", valorProcessado);

  const xhr = new XMLHttpRequest();
  xhr.open("GET", "/contato/html");

  function handleResponse() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // const resposta = JSON.parse(xhr.responseText);
      const resposta = xhr.responseText;
      console.log("resposta obtida", resposta);
      document.getElementById("div-a-ser-preenchida").innerHTML = resposta;
    } else {
      console.log("ainda não terminou", {
        state: xhr.readyState,
        status: xhr.status,
      });
    }
  }

  xhr.onreadystatechange = handleResponse;

  // xhr.setRequestHeader("content-type", "application/json");

  xhr.send();
}
