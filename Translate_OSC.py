import argparse

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from pythonosc.udp_client import SimpleUDPClient

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def send_lang_translate(message):
    client.send_message("/translation", [message])
    print(f"Sending to Client {message}")

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

model.to(device)

def print_lang_translate(unused_addr, args, inputtext,srclang,targlang):
    source_language = srclang
    target_language = targlang
    nllb_pipe = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_language, tgt_lang=target_language, max_length = 400, device=device)
    output = nllb_pipe(inputtext)[0]['translation_text']
    print(f"[{args[0]}] ~ {inputtext}")
    print(f"[{args[1]}] ~ {srclang}")
    print(f"[{args[2]}] ~ {targlang}")
    print(f"[Ouput] ~ {output}")
    send_lang_translate(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--serverport", type=int, default=5005, help="The port to for server to listen on")
    parser.add_argument("--clientport", type=int, default=5004, help="The port to send OSC client data")
    args = parser.parse_args()

    client = SimpleUDPClient(args.ip, args.clientport)

    dispatcher = Dispatcher()
    dispatcher.map("/filter", print_lang_translate, "Input","Source","Target","Ouput")

    

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.serverport), dispatcher)
    print(f"Serving on {server.server_address}")
    print(f"Sending on {client._address} {client._port}")
    server.serve_forever()