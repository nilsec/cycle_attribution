import os
import subprocess


def start_testing(nt_combinations,
                  test_nt,
                  test_setup,
                  netG="resnet_9blocks",
                  aux_checkpoint="/nrs/funke/ecksteinn/synister_experiments/gan/02_train/setup_t0/model_checkpoint_499000",
                  num_test=50,
                  train_setup=1):

    base_cmd = "~/singularity/run_lsf python -u test.py --model test --no_dropout --results_dir {} --dataroot {} --checkpoints_dir {} --name {} --model_suffix {} --num_test {} --aux_checkpoint {} --aux_input_size 128 --aux_net vgg2d --aux_input_nc 1 --num_threads 1 --verbose"
    base_dir = "/nrs/funke/ecksteinn/synister_experiments/cycle_attribution"

    if test_nt == nt_combinations[0]:
        a_or_b = "A"
    elif test_nt == nt_combinations[1]:
        a_or_b = "B"

    dataroot = base_dir + "/data_png/synister_{}_{}/train{}".format(nt_combinations[0],
                                                               nt_combinations[1],
                                                               a_or_b)
    nt_list = ["gaba", "acetylcholine", "glutamate",
               "serotonin", "octopamine", "dopamine"]

    aux_class_a = nt_list.index(nt_combinations[0])
    aux_class_b = nt_list.index(nt_combinations[1])
    train_setup_name = "train_{}_{}_s{}".format(nt_combinations[0],
                                                nt_combinations[1],
                                                train_setup)
    checkpoint_dir = base_dir + "/checkpoints"
    results_dir = base_dir + "/results/test_{}_{}_{}_t{}".format(nt_combinations[0],
                                                             nt_combinations[1],
                                                             a_or_b,
                                                             test_setup)
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    cmd = base_cmd.format(results_dir,
                          dataroot,
                          checkpoint_dir,
                          train_setup_name,
                          "_" + a_or_b,
                          num_test,
                          aux_checkpoint)

    subprocess.Popen(cmd,
                     shell=True)
    
    #subprocess.check_call(cmd,shell=True)
    #print(cmd)
def get_combinations():
    nt_list = ["gaba", "acetylcholine", "glutamate",
               "serotonin", "octopamine", "dopamine"]

    nt_combinations = []
    for ntA in nt_list:
        for ntB in nt_list:
            if ntA != ntB:
                nt_combinations.append((ntA, ntB))

    return nt_combinations

def test_all(test_setup):
    combinations = get_combinations()
    for comb in combinations:
        for nt in comb:
            start_testing(nt_combinations=comb,
                          test_nt=nt,
                          test_setup=test_setup,
                          num_test=500)

if __name__ == "__main__":
    #test_all(3)
    start_testing(nt_combinations=["acetylcholine", "dopamine"],
                  test_nt="acetylcholine",
                  test_setup=6)
