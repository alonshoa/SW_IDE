import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorchlightining as pl
import wandb
import nltk
from nltk.corpus import wikipedia
from nltk.tokenize import sent_tokenize

class WikiDataset(Dataset):
    def __init__(self):
        self.data = wikipedia.sents()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class MyGpt(pl.LightningModule):
    def __init__(self, vocab_size, embedding_dim, n_layers, n_heads, dropout, device):
        super().__init__()
        self.device = device
        self.tok_embedding = nn.Embedding(vocab_size, embedding_dim)
        self.pos_embedding = nn.Embedding(n_layers, embedding_dim)
        self.layers = nn.ModuleList([MyGptLayer(embedding_dim, n_heads, dropout, device) for _ in range(n_layers)])
        self.dropout = nn.Dropout(dropout)
        self.scale = torch.sqrt(torch.FloatTensor([embedding_dim])).to(device)

    def forward(self, x, past=None):
        seq_len, batch_size = x.size()
        position = torch.arange(seq_len, dtype=torch.long, device=self.device)
        position = position.unsqueeze(1).expand(seq_len, batch_size)
        x = self.tok_embedding(x) + self.pos_embedding(position)
        x = self.dropout(x)
        for layer in self.layers:
            x, past = layer(x, past)
        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.cross_entropy(y_hat.view(-1, y_hat.size(-1)), y.view(-1))

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-4)

    def wandb_sweep(self):
        sweep_config = {
            'method': 'random',
            'metric': {
                'name': 'val_loss',
                'goal': 'minimize'
            },
            'parameters': {
                'n_layers': {
                    'values': [1, 2, 3, 4, 5]
                }
            }
        }
        sweep_id = wandb.sweep(sweep_config, project='gpt-2')
        return sweep_id

    def train_dataloader(self):
        return DataLoader(WikiDataset(), batch_size=32)

    def on_epoch_end(self):
        wandb.log({'epoch': self.current_epoch})

class MyDataset(Dataset):
    def __init__(self):
        pass

    def __len__(self):
        return 100

    def __getitem__(self, idx):
        return torch.rand(10, 32), torch.randint(0, 10, (10, 32))
        tensorboard_logs = {'train_loss': loss}
        return {'loss': loss, 'log': tensorboard_logs}

class MyGptLayer(nn.Module):
    def __init__(self, embedding_dim, n_heads, dropout, device):
        super().__init__()
        self.attention = MyGptAttention(embedding_dim, n_heads, dropout, device)
        self.feed_forward = MyGptFeedForward(embedding_dim, dropout)

    def forward(self, x, past=None):
        x, present = self.attention(x, past=past)
        x = self.feed_forward(x)
        return x, present

class MyGptAttention(nn.Module):
    def __init__(self, embedding_dim, n_heads, dropout, device):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.n_heads = n_heads
        self.dropout = dropout
        self.device = device
        self.scale = torch.sqrt(torch.FloatTensor([self.embedding_dim // self.n_heads])).to(device)

        self.q_linear = nn.Linear(embedding_dim, embedding_dim)
        self.v_linear = nn.Linear(embedding_dim, embedding_dim)
        self.k_linear = nn.Linear(embedding_dim, embedding_dim)
        self.dropout = nn.Dropout(dropout)
        self.out = nn.Linear(embedding_dim, embedding_dim)

    def forward(self, query, past=None):
        seq_len, batch_size = query.size()
        if past is not None:
            k, v = past
            k = k.view(-1, k.size(-1))
            v = v.view(-1, v.size(-1))
            key_padding_mask = torch.zeros(k.size(0), 1, dtype=torch.bool, device=self.device)
        else:
            k = v = query
            key_padding_mask = None

        q = self.q_linear(query)
        k = self.k_linear(k)
        v = self.v_linear(v)

        q = q.view(seq_len, batch_size, self.n_heads, -1).transpose(1, 2)
        k = k.view(-1, batch_size, self.n_heads, -1).transpose(0, 1)
        v = v.view(-1, batch_size, self.n_heads, -1).transpose(0, 1)

        q = q / self.scale
        scores = torch.matmul(q, k.transpose(-2, -1))
        scores = F.softmax(scores, dim=-1)
        scores = self.dropout(scores)
        output = torch.matmul(scores, v)
        output = output.transpose(1, 2).contiguous().view(seq_len, batch_size, -1)
        output = self.out(output)
        present = torch.stack((k.view(-1, k.size(-1)), v.view(-1, v.size(-1))))
        return output, present

class MyGptFeedForward(nn.Module):
    def __init__(self, embedding_dim, dropout):
        super().__init__()
        self.linear1 = nn.Linear(embedding_dim, embedding_dim)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(embedding_dim, embedding_dim)

    def forward(self, x):
        x = self.linear1(x)
        x = self.dropout(x)
        x = self.linear2(x)
        return x

if __name__ == '__main__':
    wandb.init(project='gpt-2')
    model = MyGpt(vocab_size=100, embedding_dim=32, n_layers=1, n_heads=1, dropout=0.1, device='cpu')
    model.wandb_sweep()
