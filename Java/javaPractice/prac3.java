
class immutable {
    int k;

    public immutable(int i) {
        this.k = i;
    }

    public immutable modify(int l) {
        if (this.k == l)
            return this;
        else
            return new immutable(l);
    }
}

public class prac3 {
    public static void main(String[] args) throws Exception {
        immutable i = new immutable(23);
        immutable ii = new immutable(23);
        immutable k = i.modify(253);

        System.out.println(i == k);

    }
}