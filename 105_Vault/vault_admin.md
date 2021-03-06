# Motivation

Source: https://learn.hashicorp.com/tutorials/vault/getting-started-install?in=vault/getting-started

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get updat- [Motivation](#motivation)

sudo apt  install jq

vault -autocomplete-install

## Usage

**vault**
vault server -dev

export VAULT_ADDR='http://127.0.0.1:8200'

export VAULT_TOKEN=<token>

```{r}
vault kv put secret/hello foo=world

vault kv get secret/hello

vault kv put secret/hello foo=world excited=yes

vault kv get -field=excited secret/hello
vault kv get -format=json secret/hello | jq -r .data.data.excited

vault secrets list
```

## Starting server

```bash
vault server -config=/home/danny/vault/config.hcl

vault operator init -address=http://127.0.0.1:8200

export VAULT_ADDR='http://127.0.0.1:8200'

vault operator unseal

vault login <token>
```

```language
vault kv get kv/test
vault kv get -format=json kv/test | jq -r .data.data.test_key

export TEST=$(vault kv get -format=json kv/test | jq -r .data.data.test_key)
echo $TEST
```

## Alternative

export TEST=$(vault kv get -field=test_key kv/test)
echo $TEST

## Python

https://github.com/peopledoc/vault-cli
pip install vault-cli


sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k


sudo mv Menlo*.ttf /usr/share/fonts