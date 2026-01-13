terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.25"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}
resource "kubernetes_namespace" "clients" {
  for_each = toset(var.clients)

  metadata {
    name = each.value
  }
}
