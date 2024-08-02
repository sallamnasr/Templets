#include <iostream>
#include <vector>
#define endl "\n"
#define ll long long
using namespace std;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

ll gcd(ll x, ll y)
{
    while (x && y)
    {
        if (x > y)
        {
            x %= y;
        }
        else
            y %= x;
    }
    return x ? x : y;
}

vector<ll> divisors(ll num)
{
    vector<ll> arr;
    ll i = 1;
    while (i * i <= num)
    {
        if (num % i == 0)
        {
            arr.push_back(i);
            if (i != num / i)
            {
                arr.push_back(num / i);
            }
        }
        i++;
    }
    return arr;
}

ll lcm(ll x, ll y)
{
    if (x == 0 || y == 0)
        return -1;
    ll mul = x*y ;
    return (mul/gcd(x,y)) ;
}
ll Divisability(ll start, ll end ,ll q){
    ll number_of_nums = ((end - start )/q) +1 ;
    ll result = (number_of_nums/2)*(2*start+(number_of_nums-1)*q) ;
    return result ;
}
int main()
{
    fastIO();
    ll x, y,k;
    cin >> x >> y,k;
    cout  << Divisability(x,y,k) << endl;
    return 0;
}
