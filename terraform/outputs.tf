output "client_namespaces" {
  value = [for ns in kubernetes_namespace.clients : ns.metadata[0].name]
}
