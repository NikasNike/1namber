command = 'nul'
x = 0
while command != 'exit':
    command = input("Введите что-нибудь, чтобы проверить это: ")

    def stop_service():
        print(x + 1)

    def restart_service():
        return(x + 2)

    def start_service():
        return(x + 3)

    def set_reg_key():
        return(x + 4)

    def disable_agent_adapter_net_int():
        return(x + 5)

    def enable_agent_adapter_net_int():
        return(x + 6)
    try:
        method = {
            'stop': stop_service,
            "restart-service": restart_service(),
            "start-service": start_service(),
            "set-reg-key": set_reg_key(),
            "disable-agent-adapter-net-int": disable_agent_adapter_net_int(),
            "enable-agent-adapter-net-int": enable_agent_adapter_net_int()

        }
        method[command]()
    except LookupError:
        print("исключение")
    else:
        print("успех")

    
    
print("вы вышли((()))")
    
