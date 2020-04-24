Cycle GAN clone from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix with additional auxiliary losses

~/singularity/run_lsf python -u train.py --aux_checkpoint /nrs/funke/ecksteinn/synister_experiments/gan/02_train/setup_t0/model_checkpoint_499000 --aux_class_A 1 --aux_class_B 3 --aux_lambda_class_A 10 --aux_lambda_class_B 10 --dataroot datasets/synister_ach_ser/ --name ach_ser_1_3_auxlA10_auxlB10 --input_nc 1 --output_nc 1
