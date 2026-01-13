variable "clients" {
  description = "List of client namespaces"
  type        = list(string)
  default     = ["client-a", "client-v", "client-c"]
}
