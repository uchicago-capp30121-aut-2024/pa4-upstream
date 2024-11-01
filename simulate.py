'''
CAPP 121: PA #4 Polling Places

NAME: YOUR NAME(S) HERE

Main file for plling place simulation
'''

import sys
import util
import random
import queue
import click


class Voter:
    """Class for representing a voter"""
    # YOUR Voter class GOES HERE


class VotingBooths:
    '''Class for representing a bank of voting booths

    Attributes: None

    Methods:
        is_booth_available (bool):
            Is there at least one unoccupied booth
        is_some_booth_occupied (bool):
            Is there at least one occupied booth
        time_next_free() (float):
            When will a booth be free next (only called when all the
                booths are occupied)
        enter_booth(v) (Voter):
            Add a voter to a booth (only caclled when a booth is available)
        exit_booth():
            Remove the next voter to depart from the booths and
                return the their departure time
    '''

    def __init__(self, num_booths):
        '''
        Initialize the voting booths

        Args:
            num_booths (int): The number of voting booths in the bank
        '''
        self._q = queue.PriorityQueue()
        self._num_booths = num_booths

    def is_booth_available(self):
        '''Is at least one booth open'''
        return self._q.qsize() < self._num_booths

    def is_some_booth_occupied(self):
        '''Is at least one booth occupied'''
        return self._q.qsize() > 0

    def time_next_free(self):
        '''
        When will the next voter leave?

        Returns (float): The next departure time

        Requirements: There must be at least one occupied booth
        '''
        assert self.is_some_booth_occupied(), "No booths in use"

        # PriorityQueue does not have a peek method.
        # So, do a get followed by a put.
        (dt, v) = self._q.get()
        self._q.put((dt, v))
        return dt

    def enter_booth(self, v):
        '''
        Add voter v to an open booth

        Inputs:
            v (Voter): The voter to add to the booth

        Requirements: There must be an open booth
        '''
        assert self.is_booth_available(), "All booths in use"
        assert v.start_time, "Voter's start time must be set"

        dt = v.start_time + v.voting_duration
        v.departure_time = dt
        self._q.put((dt, v))

    def exit_booth(self):
        '''
        Remove voter with lowest departure time

        Returns (float): The voter's departure time

        Requirements: There must be at least one occupied booth
        '''
        assert self.is_some_booth_occupied(), "No booths in use"

        (dt, v) = self._q.get()
        return dt


class Precinct:

    def __init__(self, name, hours_open, max_num_voters, 
                 arrival_rate, voting_duration_rate):
        '''
        Constructor for the Precint class

        Input:
            name (str): Name of the precinct
            hours_open (int): Hours the precinct will remain open
            max_num_voters (int): Number of voters in the precinct
            arrival_rate (float): Rate at which voters arrive
            voting_duration_rate (float): Lambda for voting duration
        '''
        # YOUR CODE HERE

        # REPLACE "pass" with your code
        pass

    def simulate(self, seed, num_booths):
        '''
        Simulate election day for the precinct using the specified seed 
            and number of voting booths

        Args:
            seed (int): The seed for the random number generator
            num_booths (int): The number of voting booths assigned to the
                precinct for the day

        Returns (list of Voter): The list of Voters
        '''
        # YOUR CODE HERE

        # REPLACE [] with appropriate return value
        return []



def find_avg_wait_time(precinct, num_booths, ntrials, initial_seed=0):
    '''
    Simulates a precinct multiple times with a given number of booths. 
        For each simulation, computes the average waiting time of the voters,
        and returns the median of those average waiting times

    Input:
        precinct (dictionary): A precinct configuration dictionary
        num_booths (int): The number of booths to simulate the precinct with
        ntrials (int): The number of trials to run
        initial_seed (int): The initial seed for random number generator

    Returns (float):
        The median of the average waiting times returned by simulating
        the precinct 'ntrials' times
    '''

    # YOUR CODE HERE

    # Replace None with a suitable return value
    return None


def find_number_of_booths(precinct, target_wait_time, max_num_booths, ntrials, seed=0):
    '''
    Finds the number of booths a precinct needs to guarantee a bounded
    (average) waiting time

    Input:
        precinct (dictionary): A precinct dictionary
        target_wait_time (float): The desired (maximum) waiting time
        max_num_booths (int): The maximum number of booths this precinct can support
        ntrials (int): The number of trials to run when computing 
            the average waiting time                 
        seed (int): A random seed

    Output:
        A tuple (num_booths, waiting_time) where:
        num_booths (int): The smallest number of booths that ensures
            the average waiting time is below target_waiting_time
        waiting_time (float): The actual average waiting time with that
            number of booths
        If the target waiting time is infeasible, returns (0, None)
    '''
    # YOUR CODE HERE

    # Replace None, 0 with a suitable return value
    return None, 0


@click.command(name="simulate")
@click.argument('precincts_file', type=click.Path(exists=True))
@click.option('--max-num-booths', type=int)
@click.option('--target-wait-time', type=float)
@click.option('--print-voters', is_flag=True)
def cmd(precincts_file, max_num_booths, target_wait_time, print_voters):
    p, seed = util.load_precinct(precincts_file)

    if target_wait_time is None:
        voters = {}
        precinct = Precinct(p["name"],
                            p["hours_open"],
                            p["num_voters"],
                            p["arrival_rate"],
                            p["voting_duration_rate"])
        voters[p["name"]] = precinct.simulate(seed, p["num_booths"])
        print()
        if print_voters:
            for p, v in voters.items():
                print(f"PRECINCT '{p}'")
                util.print_voters(v)
                print()
        else:
            pname = p["name"]
            if pname not in voters:
                print(f"ERROR: Precinct file specified a '{pname}' precinct")
                print("       But simulate_election_day returned no such precinct")
                print()
                sys.exit(-1)
            pvoters = voters[pname]
            if len(pvoters) == 0:
                print(f"Precinct '{pname}': No voters voted")
            else:
                pl = "s" if len(pvoters) > 1 else ""
                closing = p["hours_open"]*60.
                last_depart = pvoters[-1].departure_time
                avg_wt = sum([v.start_time - v.arrival_time for v in pvoters]) / len(pvoters)
                print(f"PRECINCT '{pname}'")
                print(f"- {len(pvoters)} voter{pl} voted")
                msg = "- Polls closed at {} and last voter departed at {:.2f}"
                print(msg.format(closing, last_depart))
                print(f"- Avg wait time: {avg_wt:.2f}")
                print()
    else:
        precinct = p

        if max_num_booths is None:
            max_num_booths = precinct["num_voters"]

        nb, avg_wt = find_number_of_booths(precinct, target_wait_time, max_num_booths, 20, seed)

        if nb == 0:
            msg = "The target wait time ({:.2f}) is infeasible"
            msg += " in precint '{}' with {} or less booths"
            print(msg.format(target_wait_time, precinct["name"], max_num_booths))
        else:
            msg = "Precinct '{}' can achieve average waiting time"
            msg += " of {:.2f} with {} booths"
            print(msg.format(precinct["name"], avg_wt, nb))


if __name__ == "__main__":
    cmd() # pylint: disable=no-value-for-parameter
