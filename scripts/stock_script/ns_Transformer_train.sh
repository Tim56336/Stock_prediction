python -u run.py \
  --is_training 1 \
  --root_path ./data/stock/ \
  --data_path stock01.csv \
  --model_id Stock2330 \
  --model ns_Transformer \
  --data custom \
  --features M \
  --seq_len 30 \
  --label_len 0 \
  --pred_len 1 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 4 \
  --dec_in 4 \
  --c_out 4 \
  --gpu 0 \
  --des 'stock2330' \
  --p_hidden_dims 256 256 \
  --p_hidden_layers 2 \
  --itr 1  \
  --do_predict  \


